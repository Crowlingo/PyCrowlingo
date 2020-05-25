from pydantic import BaseModel

from . import Responses
from ..Attributes import Document, Visualize
from ..Basic import BasicModel
from .Examples import Requests as Examples


class Base(BasicModel):
    _prefix = "/entities"
    _response_module = Responses


class Extract(Examples.Extract, Base, Document):
    class Query(Visualize):
        pass


class Duckling(Examples.Duckling, Base, Document):
    class Query(BaseModel):
        pass
