from pydantic import BaseModel

from . import Responses
from .Examples import Requests as Examples
from ..Basic import BasicModel


class Base(BasicModel):
    _prefix = "/languages"
    _response_module = Responses


class Detect(Examples.Detect, Base):
    text: str

    class Query(BaseModel):
        pass

