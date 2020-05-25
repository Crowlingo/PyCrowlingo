from typing import Dict, Any, List

from pydantic import BaseModel

from .Examples import Responses as Examples


class Pipeline(Examples.Pipeline):
    responses: Dict[str, Any]


class Bulk(BaseModel):
    responses: List[Dict[str, Any]]
