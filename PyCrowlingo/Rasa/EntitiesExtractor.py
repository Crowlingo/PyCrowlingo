import typing
from typing import Any, Optional, Text, Dict

from rasa.nlu.constants import ENTITIES
from rasa.nlu.extractors.extractor import EntityExtractor
from rasa.nlu.training_data import Message

from .. import Client

if typing.TYPE_CHECKING:
    pass


class EntitiesExtractor(EntityExtractor):
    """Retrieve named entities from 18 types in 100+ languages"""

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
        self.client = Client(component_config["token"])

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
        res = self.client.entities.extract(message.text)
        entities = [
            {
                "entity": ent.ent_type,
                "value": ent.text,
                "start": ent.start,
                "confidence": None,
                "end": ent.end,
            }
            for ent in res.entities
        ]
        extracted = self.add_extractor_name(entities)
        message.set(ENTITIES, message.get(ENTITIES, []) + extracted, add_to_output=True)
