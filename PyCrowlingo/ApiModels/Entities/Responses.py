from typing import List, Dict, Any

from .Examples import Responses as Examples
from ..Attributes import Entities, Visualization


class Extract(Examples.Extract, Entities, Visualization):
    pass


class Duckling(Examples.Duckling):
    duckling: List[Dict[str, Any]]

