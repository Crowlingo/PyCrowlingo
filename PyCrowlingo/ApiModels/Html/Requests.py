from pydantic import BaseModel
from pydantic import AnyUrl

from . import Responses
from .Examples import Requests as Examples
from ..Basic import BasicModel


class Base(BasicModel):
    _prefix = "/html"
    _response_module = Responses


class ExtractArticle(Examples.ExtractArticle, Base):
    url: AnyUrl

    class Query(BaseModel):
        pass
