from typing import List

from .Examples import Responses as Examples
from ..Attributes import SentenceSyntax, Visualization


class Extract(Examples.Extract, Visualization):
    sentences: List[SentenceSyntax]

