from ..Basic import BasicModel
from . import Responses
from .Examples import Requests as Examples


class Base(BasicModel):
    _prefix = "/user"
    _response_module = Responses
    _method = "GET"
    _price = 0


class Login(Examples.Login, Base):
    pass


class RefreshToken(Examples.RefreshToken, Base):
    pass


class Usage(Examples.Usage, Base):
    pass


class Info(Examples.Info, Base):
    pass
