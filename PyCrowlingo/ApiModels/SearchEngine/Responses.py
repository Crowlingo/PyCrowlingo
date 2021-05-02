from .Examples import Responses as Examples
from ..Attributes import LangSearchResult, DocumentsId


class Search(Examples.Search, LangSearchResult):
    pass


class CreateDocuments(Examples.CreateDocuments, DocumentsId):
    pass


class CreateKeywords(Examples.CreateKeywords, DocumentsId):
    pass


class DeleteDocuments(Examples.DeleteDocuments, DocumentsId):
    pass
