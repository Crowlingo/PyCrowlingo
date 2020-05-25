from typing import Optional

from pydantic import BaseModel

from . import Responses
from .Examples import Requests as Examples
from ..Attributes import Document
from ..Basic import BasicModel


class Base(BasicModel):
    _prefix = "/summary"
    _response_module = Responses


class Extract(Examples.Extract, Base, Document):

    class Query(BaseModel):
        ratio: float = 0.01
        nb_sentences: Optional[int] = None
