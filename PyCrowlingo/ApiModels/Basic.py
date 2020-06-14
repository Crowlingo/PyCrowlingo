import re
from collections import defaultdict

from pydantic import BaseModel

from .. import Errors

HEADERS = {
    "x-cur-minute": {"description": "Counter of requests made during this minute", "schema": {"type": "string"}},
    "x-cur-period": {"description": "Counter of requests made during this period", "schema": {"type": "string"}},
    "x-minute-limit": {"description": "Limit number of requests in one minute", "schema": {"type": "string"}},
    "x-period-limit": {"description": "Limit number of requests in one period", "schema": {"type": "string"}},
    "x-minute-reset": {"description": "Seconds until the minute counter reset", "schema": {"type": "string"}},
    "x-period-reset": {"description": "Seconds until the period counter reset", "schema": {"type": "string"}},
    "x-query-price": {"description": "Number of requests consumed by this query", "schema": {"type": "integer"}},
}


NO_HEADERS_STATUS = [401, 403, 422, 500]
BASIC_STATUS = [200, 401, 422]


class BasicModel(BaseModel):
    _response_module = None
    _response_error = None
    _include_in_schema = True
    _prefix = ""
    _method = "POST"
    _endpoint = None
    _query = {}
    _rbm = {}
    _price = 1
    _responses = []

    class Query(BaseModel):
        pass

    class Config:
        pass

    @classmethod
    def eid(cls):
        return f"[{cls._method}] {cls.endpoint()}"

    @classmethod
    def rbm(cls):
        return '_'.join(cls.endpoint().split('/')[1:])

    @classmethod
    def endpoint(cls):
        res = cls._endpoint
        if res is None:
            name = cls.__name__
            s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
            res = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
        elif not res:
            return cls._prefix
        return cls._prefix + "/" + res

    @classmethod
    def get_price(cls):
        return cls._price

    @classmethod
    def get_response_model(cls):
        return getattr(cls._response_module, cls.__name__)

    @classmethod
    def get_responses(cls):
        res = defaultdict(dict)
        for status in cls._responses + BASIC_STATUS:
            if status not in NO_HEADERS_STATUS:
                res[status]["headers"] = HEADERS
            res[status]["model"] = Errors.CrowlingoExceptionModel
        return res

    @classmethod
    def route(cls):
        return {
            "path": cls.endpoint(),
            "response_model": cls.get_response_model(),
            "responses": cls.get_responses(),
            "response_model_skip_defaults": True,
            "include_in_schema": cls._include_in_schema,
            "methods": [cls._method]
        }

    def call(self, client, username=None, password=None):
        body = {k: v for k, v in self.dict().items() if v is not None}
        endpoint = self.endpoint()
        query = {}
        path = {}
        for k, v in self._query.items():
            if v is not None:
                if f'{{{k}}}' in endpoint:
                    path[k] = v
                else:
                    query[k] = v
        endpoint = endpoint.format_map(path)
        auth = (username, password) if username and password else None
        response = client.call(endpoint=endpoint, params=query, json=body, method=self._method, auth=auth)
        return self.get_response_model()(**response)

    @classmethod
    def fill(cls, **params):
        args = {k: v for k, v in params.items() if v is not None and k != "self"}
        res = cls(**args)
        res._query.clear()
        res._query.update(res.Query(**args).dict())
        if res._endpoint:
            res._endpoint.format(**args)
        return res

    def fulldict(self):
        res = self.dict()
        res.update(self._query)
        return res

    @classmethod
    def x_code_example_python(cls):
        lines = getattr(cls.Config, "schema_extra", {}).get("_python", [])
        return '\n'.join(lines)

    @classmethod
    def x_code_examples(cls):
        return [{"lang": "Python", "source": cls.x_code_example_python()}]
