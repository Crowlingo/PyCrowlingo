import typing
from collections import defaultdict
from typing import Any, Optional, Text, Dict

from PyCrowlingo.Errors import ModelNotFound
from rasa.nlu.extractors.extractor import EntityExtractor
from rasa.nlu.training_data import Message, TrainingData
from rasa.nlu.config import RasaNLUModelConfig
from rasa.nlu.constants import ENTITIES
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

    def __init__(self, component_config: Optional[Dict[Text, Any]] = None) -> None:
        super().__init__(component_config)
        self.client = get_client(component_config)
        self.lang = component_config.get("lang")
        self.properties = component_config.get("properties")
        self.model_owner = component_config.get("model_owner")
        self.model_id = component_config.get("model_id")
        self.prod_version = component_config.get("prod_version")
        self.precision = component_config.get("precision")

    def train(self, training_data: TrainingData, config: Optional[RasaNLUModelConfig] = None, **kwargs: Any) -> None:
        try:
            self.client.model.clear(self.model_id, model_owner=self.model_owner, prod_version=self.prod_version)
        except ModelNotFound:
            self.client.model.create(self.model_id, "cpt")
            self.model_owner = None
            self.prod_version = None
        concepts = defaultdict(set)
        synonyms = defaultdict(set)
        for key, value in training_data.entity_synonyms.items():
            synonyms[key].add(value)
        for msg in training_data.entity_examples:
            for entity in msg.get(ENTITIES, []):
                label = str(entity.get("value"))
                concept = str(entity.get("entity"))
                concepts[concept].add(label)
                if label in synonyms:
                    concepts[concept] |= synonyms.pop(label)
        self.client.concepts.create_concepts(self.model_id, concepts=[{"id": concept} for concept in concepts.keys()],
                                             model_owner=self.model_owner)
        self.client.concepts.create_labels(self.model_id,
                                           labels=[{"text": label, "concept_id": concept}
                                                   for concept, labels in concepts.items() for label in labels],
                                           model_owner=self.model_owner)
        self.client.model.train(self.model_id, model_owner=self.model_owner)
        self.client.model.wait_training(self.model_id, model_owner=self.model_owner)

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
        res = self.client.concepts.extract_custom(text=message.text, lang=self.lang,
                                                  properties=self.properties,
                                                  model_owner=self.model_owner,
                                                  model_id=self.model_id,
                                                  prod_version=self.prod_version)
        concepts = []
        for concept in res.concepts:
            for label in concept.labels:
                for mention in label.mentions:
                    concepts.append({
                        "entity": concept.id,
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
