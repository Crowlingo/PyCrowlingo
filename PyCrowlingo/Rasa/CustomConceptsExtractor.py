import typing
from collections import defaultdict
from typing import Any, Optional, Text, Dict

from PyCrowlingo.Errors import ModelNotFound
from rasa.nlu.extractors.extractor import EntityExtractor
from rasa.nlu.config import RasaNLUModelConfig
from rasa.shared.nlu.constants import ENTITIES, TEXT
from rasa.shared.nlu.training_data.message import Message
from rasa.shared.nlu.training_data.training_data import TrainingData
import rasa.utils.io as io_utils
from rasa.nlu.model import Metadata
from PyCrowlingo.ApiModels.Attributes import ID_TYPE
from pydantic.errors import StrRegexError
import os

from uuid import uuid4
from .Utils import get_client

if typing.TYPE_CHECKING:
    pass


class CustomConceptsExtractor(EntityExtractor):
    """Link the entities with wikipedia pages and get additional """

    # Defines the default configuration parameters of a component
    # these values can be overwritten in the pipeline configuration
    # of the model. The component should choose sensible defaults
    # and should be able to create reasonable results with the defaults.
    defaults = {}

    # Defines what language(s) this component can handle.
    # This attribute is designed for instance method: `can_handle_language`.
    # Default value is None which means it can handle all languages.
    # This is an important feature for backwards compatibility of components.
    language_list = None

    def __init__(self, component_config: Optional[Dict[Text, Any]] = None,
                 concept_encoder: Optional[Dict[Text, Any]] = None) -> None:
        super().__init__(component_config)
        self.client = get_client(component_config)
        self.lang = component_config.get("lang")
        self.properties = component_config.get("properties")
        self.model_id = component_config.get("model_id")
        self.prod_version = component_config.get("prod_version")
        self.precision = component_config.get("precision")
        self.concept_encoder = concept_encoder or {}

    def train(self, training_data: TrainingData, config: Optional[RasaNLUModelConfig] = None, **kwargs: Any) -> None:
        try:
            self.client.model.clear(self.model_id)
        except ModelNotFound:
            self.client.model.create(self.model_id, "concepts")
            self.prod_version = None
        concept_to_id = {}
        concepts = defaultdict(set)
        synonyms = defaultdict(set)
        for key, value in training_data.entity_synonyms.items():
            synonyms[key].add(value)
        for msg in training_data.entity_examples:
            for entity in msg.get(ENTITIES, []):
                label = str(entity.get("value"))
                concept = str(entity.get("entity"))
                try:
                    ID_TYPE.validate(concept)
                    concept_id = concept
                except StrRegexError:
                    concept_id = concept_to_id.get(concept)
                    if not concept_id:
                        concept_id = uuid4()
                        concept_to_id[concept] = concept_id
                concepts[concept].add(label)
                if label in synonyms:
                    concepts[concept] |= synonyms.pop(label)
        self.client.concepts.create_concepts(self.model_id, concepts=[{"id": concept} for concept in concepts.keys()])
        self.client.concepts.create_labels(self.model_id,
                                           labels=[{"text": label, "concept_id": concept}
                                                   for concept, labels in concepts.items() for label in labels])
        self.client.model.train(self.model_id)
        self.client.model.wait_training(self.model_id)
        self.concept_encoder = {v: k for k, v in concept_to_id.items()}

    def process(self, message: Message, **kwargs: Any) -> None:
        """Process an incoming message.

        This is the components chance to process an incoming
        message. The component can rely on
        any context attribute to be present, that gets created
        by a call to :meth:`components.Component.pipeline_init`
        of ANY component and
        on any context attributes created by a call to
        :meth:`components.Component.process`
        of components previous to this one."""
        res = self.client.concepts.extract_custom(text=message.get(TEXT), lang=self.lang,
                                                  properties=self.properties,
                                                  model_id=self.model_id,
                                                  prod_version=self.prod_version)
        concepts = []
        for concept in res.concepts:
            for label in concept.labels:
                for mention in label.mentions:
                    concepts.append({
                        "entity": self.concept_encoder.get(concept.id, concept.id),
                        "value": label.text,
                        "start": mention.start,
                        "end": mention.end,
                        "confidence": mention.similarity,
                        "properties": concept.properties,
                    })
        all_extracted = self.add_extractor_name(concepts)
        dimensions = self.component_config.get("dimensions")
        extracted = self.filter_irrelevant_entities(all_extracted, dimensions)
        extracted = self.add_extractor_name(extracted)
        message.set(ENTITIES, message.get(ENTITIES, []) + extracted, add_to_output=True)

    def persist(self, file_name: Text, model_dir: Text) -> Optional[Dict[Text, Any]]:
        """Persist this model into the passed directory."""

        concept_encoder_file_name = file_name + "concept_encoder.pkl"
        if self.concept_encoder:
            io_utils.json_pickle(os.path.join(model_dir, concept_encoder_file_name), self.concept_encoder)
        return {"concept_encoder": concept_encoder_file_name}

    @classmethod
    def load(cls, meta: Dict[Text, Any], model_dir: Optional[Text] = None, model_metadata: Optional[Metadata] = None,
        cached_component: Optional["SklearnIntentClassifier"] = None, **kwargs: Any) -> "SklearnIntentClassifier":
        concept_encoder_file = os.path.join(model_dir, meta.get("concept_encoder"))
        if os.path.exists(concept_encoder_file):
            concept_encoder = io_utils.json_unpickle(concept_encoder_file)
            return cls(meta, concept_encoder)
        else:
            return cls(meta)