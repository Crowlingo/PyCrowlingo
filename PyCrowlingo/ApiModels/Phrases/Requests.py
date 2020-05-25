from typing import Optional, Dict, Any

from pydantic import BaseModel

from . import Responses
from .Examples import Requests as Examples
from ..Attributes import Document, Visualize
from ..Basic import BasicModel


class Base(BasicModel):
    _prefix = "/phrases"
    _response_module = Responses


class ExtractKeys(Examples.ExtractKeys, Base, Document):
    class Query(BaseModel):
        normalize: Optional[str]
        limit: Optional[int] = 10


class Match(Examples.Match, Base, Document):
    phrase: str
    phrase_lang: Optional[str] = None

    class Query(Visualize):
        precision: float = 0.75


class RuleBasedMatch(Base, Document):
    patterns: Dict[str, str]
    parameters: Optional[Dict[str, Any]] = {}
    sentence_isolation: bool = True
    greedy: bool = True

    class Query(BaseModel):
        visualize: bool = False
