import typing
from typing import Any, Optional, Text, Dict

from rasa.nlu.extractors.extractor import EntityExtractor
from rasa.shared.nlu.constants import ENTITIES, TEXT
from rasa.shared.nlu.training_data.message import Message

from .Utils import get_client

if typing.TYPE_CHECKING:
    pass


class DucklingExtractor(EntityExtractor):
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
        self.client = get_client(component_config)

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

        matches = self.client.entities.duckling(message.get(TEXT)).duckling
        all_extracted = self.convert_duckling_format_to_rasa(matches)
        dimensions = self.component_config.get("dimensions")
        extracted = self.filter_irrelevant_entities(all_extracted, dimensions)
        extracted = self.add_extractor_name(extracted)
        message.set(ENTITIES, message.get(ENTITIES, []) + extracted, add_to_output=True)

    def extract_value(self, match: Dict[Text, Any]) -> Dict[Text, Any]:
        if match["value"].get("type") == "interval":
            value = {
                "to": match["value"].get("to", {}).get("value"),
                "from": match["value"].get("from", {}).get("value"),
            }
        else:
            value = match["value"].get("value")

        return value

    def convert_duckling_format_to_rasa(self, matches: typing.List[Dict[Text, Any]]) -> typing.List[Dict[Text, Any]]:
        extracted = []
        for match in matches:
            value = self.extract_value(match)
            entity = {
                "start": match["start"],
                "end": match["end"],
                "text": match.get("body", match.get("text", None)),
                "value": value,
                "confidence": 1.0,
                "additional_info": match["value"],
                "entity": match["dim"],
            }
            extracted.append(entity)
        return extracted