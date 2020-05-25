from typing import Optional

from pydantic import BaseModel

from . import Responses
from .Examples import Requests as Examples
from ..Attributes import Document
from ..Basic import BasicModel


class Base(BasicModel):
    _prefix = "/texts"
    _response_module = Responses


class Similarity(Examples.Similarity, Base, Document):
    text2: str
    lang2: Optional[str]

    class Query(BaseModel):
        pass
