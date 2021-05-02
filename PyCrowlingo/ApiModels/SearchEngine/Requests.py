from typing import List

from pydantic import Field

from . import Responses
from .Examples import Requests as Examples
from ..Attributes import ModelId, Document, Text, Languages, DocumentsId, SearchEngineKeyword
from ..Basic import BasicModel


class Base(BasicModel):
    _prefix = "/search_engine"
    _response_module = Responses
    _price = 0


class Search(Examples.Search, Base, Text, Languages):  # Completeness
    _endpoint = "{model_id}/search"
    _price = 1
    _responses = [400, 404]
    precision: float = Field(0, description="Precision limit. if a keyword has lower confidence, it will not be "
                                            "included in the results")

    class Query(ModelId):
        limit: int = Field(1, description="Number of results for each languages")


class CreateDocuments(Examples.CreateDocuments, Base):
    _endpoint = "{model_id}/documents"
    _responses = [403, 404, 409, 411, 413]
    documents: List[Document]
    light: bool = Field(False, description="Light preprocessing of the text for keywords extraction. "
                                           "Allows faster indexing of documents.")

    class Query(ModelId):
        pass


class CreateKeywords(Examples.CreateKeywords, Base):
    _endpoint = "{model_id}/keywords"
    _responses = [403, 404, 409, 411, 413]
    keywords: List[SearchEngineKeyword]

    class Query(ModelId):
        pass


class DeleteDocuments(Examples.DeleteDocuments, Base, DocumentsId):
    _endpoint = "{model_id}/documents"
    _responses = [403, 404, 409, 411, 413]
    _method = "DELETE"

    class Query(ModelId):
        pass
