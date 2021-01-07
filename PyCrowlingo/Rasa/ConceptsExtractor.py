import typing
from typing import Any, Optional, Text, Dict

from rasa.nlu.extractors.extractor import EntityExtractor
from rasa.shared.nlu.constants import TEXT
from rasa.shared.nlu.training_data.message import Message

from .Utils import get_client

if typing.TYPE_CHECKING:
    pass


class ConceptsExtractor(EntityExtractor):
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
        self.split = component_config.get("split")
        self.precision = component_config.get("precision")

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
        res = self.client.concepts.extract(message.get(TEXT), lang=self.lang,
                                           properties=self.properties,
                                           split=self.split,
                                           precision=self.precision)
        concepts = []
        for concept in res.concepts:
            for label in concept.labels:
                for mention in label.mentions:
                    concepts.append({
                        "value": label.text,
                        "start": mention.start,
                        "end": mention.end,
                        "entity": concept.id,
                        "properties": concept.properties,
                        "confidence": concept.weight
                    })
        all_extracted = self.add_extractor_name(concepts)
        dimensions = self.component_config.get("dimensions")
        extracted = self.filter_irrelevant_entities(all_extracted, dimensions)
        extracted = self.add_extractor_name(extracted)
        message.set("concepts", message.get("concepts", []) + extracted, add_to_output=True)
