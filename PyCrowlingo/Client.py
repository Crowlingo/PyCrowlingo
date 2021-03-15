import time
from json import JSONDecodeError

import requests
from lazy import lazy
from requests import HTTPError

from . import Errors
from .Classifier import Classifier
from .Concepts import Concepts
from .Entities import Entities
from .Errors import CrowlingoException, InternalError
from .Faq import Faq
from .Html import Html
from .Languages import Languages
from .Model import Model
from .Phrases import Phrases
from .Summary import Summary
from .Syntax import Syntax
from .Texts import Texts
from .User import User


class Client:

    def __init__(self, token=None, username=None, password=None, url="https://crowlingo.com/api/v1",
                 throttling_management=True, retry=3, verbose=True):
        self._url = url
        self._token = token
        self._throttling_management = throttling_management
        self._retry = retry
        self._plan = None
        self._verbose = verbose
        self.get_token(username, password)

    def get_token(self, username=None, password=None):
        if self._token is None and username is None and password is None:
            e = CrowlingoException(401, "Token or identifiers not set")
            raise e
        elif self._token is None:
            self.user.login(username, password)
        return self._token

    def get_plan(self):
        return self._plan

    def set_token(self, token):
        self._token = token

    def call(self, endpoint, method, auth=None, params=None, json=None, retry=0):
        recall = False
        exception = None
        headers = {'x-api-key': self.get_token()} if not auth else None
        url = f'{self._url}{endpoint}'
        res = requests.request(method=method, url=url, auth=auth,
                               headers=headers, params=params, json=json)
        try:
            res.raise_for_status()
        except HTTPError:
            status_code = res.status_code
            if status_code != 500:
                try:
                    res_json = res.json()
                    detail = res_json.get("detail", {})
                except JSONDecodeError:
                    raise CrowlingoException(status_code, res.text)
            else:
                detail = InternalError().detail
            error_id = detail.get("error_id")
            msg = detail.get("msg")
            if error_id in Errors.ErrorsEnum.__members__:
                new_e = Errors.ErrorsEnum[error_id]
                if new_e == Errors.ErrorsEnum.MINUTE_LIMIT_REACHED:
                    wait = int(res.headers.get("x-minute-reset"))
                    if self._verbose:
                        print(f"Minute limit reached: waiting {wait} seconds")
                    time.sleep(wait)
                    recall = True
                if new_e == Errors.ErrorsEnum.INTERNAL_ERROR:
                    recall = True
                new_e = new_e.value()
                new_e.status_code = status_code
                new_e.detail["msg"] = msg
            else:
                new_e = CrowlingoException(status_code, msg)
            exception = new_e
        if recall:
            retry += 1
            if retry <= self._retry:
                return self.call(endpoint, method, auth, params, json, retry)
        if exception:
            raise exception
        return res.json()

    @lazy
    def concepts(self):
        return Concepts(self)

    @lazy
    def entities(self):
        return Entities(self)

    @lazy
    def faq(self):
        return Faq(self)

    @lazy
    def html(self):
        return Html(self)

    @lazy
    def classifier(self):
        return Classifier(self)

    @lazy
    def languages(self):
        return Languages(self)

    @lazy
    def model(self):
        return Model(self)

    @lazy
    def phrases(self):
        return Phrases(self)

    @lazy
    def summary(self):
        return Summary(self)

    @lazy
    def syntax(self):
        return Syntax(self)

    @lazy
    def texts(self):
        return Texts(self)

    @lazy
    def user(self):
        return User(self)
