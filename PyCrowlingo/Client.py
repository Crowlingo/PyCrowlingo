import time

import requests
from lazy import lazy
from requests import HTTPError

from .Classifier import Classifier
from .Concepts import Concepts
from .Entities import Entities
from .Faq import Faq
from .Html import Html
from .Languages import Languages
from .Phrases import Phrases
from .Summary import Summary
from .Syntax import Syntax
from .Texts import Texts
from .User import User


class Client:

    def __init__(self, token=None, username=None, password=None, url="https://crowlingo.com/api/v1", retry=3,
                 time_retry=10):
        self._url = url
        self._token = token
        self._retry = retry
        self._time_retry = time_retry
        # self._decode_token()
        self.get_token(username, password)
        # self._decode_token()

    def get_token(self, username=None, password=None):
        if self._token is None and username is None and password is None:
            detail = "Token or identifiers not set"
            status_code = 401
            e = HTTPError(detail, status_code)
            e.detail = detail
            e.status_code = status_code
            raise e
        elif self._token is None:
            self.user.login(username, password)
        return self._token

    def set_token(self, token):
        self._token = token

    def call(self, endpoint, method, auth=None, params=None, json=None, retry=0):
        headers = {'x-api-key': self.get_token()} if not auth else None
        url = f'{self._url}{endpoint}'
        res = requests.request(method=method, url=url, auth=auth,
                               headers=headers, params=params, json=json)
        try:
            if res.status_code == 429 or res.status_code == 500:
                retry += 1
                if retry <= self._retry:
                    if res.status_code != 500:
                        time.sleep(self._time_retry)
                    return self.call(endpoint, method, auth, params, json, retry)
            res.raise_for_status()
        except Exception as e:
            detail = res.json().get("detail")
            if detail:
                new_e = type(e)(f"{str(e)}: {detail}")
                new_e.status_code = res.status_code
                new_e.detail = detail
                raise new_e
            raise e
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
