from pydantic import BaseModel, conlist

from . import Responses
from .Examples import Requests as Examples
from ..Attributes import CommonsPipeline
from ..Basic import BasicModel


class Base(BasicModel):
    _prefix = "/multi"
    _response_module = Responses


class Pipeline(Examples.Pipeline, Base, CommonsPipeline):

    class Query(BaseModel):
        pass


class Bulk(Base):
    pipelines: conlist(CommonsPipeline, max_items=20)

    class Query(BaseModel):
        pass
