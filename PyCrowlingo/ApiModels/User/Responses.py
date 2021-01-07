from typing import List

from .Examples import Responses as Examples
from ..Attributes import ModelInfo


class Usage(Examples.Usage):
    cur_minute: int
    cur_period: int
    minute_limit: int
    period_limit: int
    models_limit: int
    minute_reset: str
    period_reset: str


class Login(Examples.Login):
    access_token: str
    plan: str


class RefreshToken(Examples.RefreshToken):
    access_token: str


class Info(Examples.Info):
    email: str
    plan: str
