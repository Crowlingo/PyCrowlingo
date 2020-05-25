from typing import List, Dict, Optional

from pydantic import BaseModel

from .Examples import Responses as Examples
from .. import Attributes
from ..Attributes import KeyPhrase, PhraseMatch, Visualization


class ExtractKeys(Examples.ExtractKeys, BaseModel):
    key_phrases: List[KeyPhrase]


class Match(Examples.Match, Visualization):
    matches: List[PhraseMatch]


class RuleBasedMatch(BaseModel):
    matches: Dict[str, List[Attributes.Match]]
    visualization: Optional[str] = None
