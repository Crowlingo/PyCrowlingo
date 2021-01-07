from typing import List

from .Examples import Responses as Examples
from ..Attributes import ClassDetection, DocumentsId, DocumentId, DocumentModel, ModelInfo


class Classify(Examples.Classify):
    classes: List[ClassDetection]


class CreateDocuments(Examples.CreateDocuments, DocumentsId):
    pass


class DeleteDocument(Examples.DeleteDocument, DocumentId):
    pass


class UpdateDocument(Examples.UpdateDocument, DocumentId):
    pass


class GetDocument(Examples.GetDocument, DocumentModel):
    pass


class ListDocuments(Examples.ListDocuments):
    documents: List[DocumentModel]


class RenameClass(Examples.RenameClass, ModelInfo):
    pass
