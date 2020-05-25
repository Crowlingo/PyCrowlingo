from . import Responses
from .Examples import Requests as Examples
from ..Attributes import Document, Visualize
from ..Basic import BasicModel


class Base(BasicModel):
    _prefix = "/syntax"
    _response_module = Responses


class Extract(Examples.Extract, Base, Document):
    class Query(Visualize):
        pass

