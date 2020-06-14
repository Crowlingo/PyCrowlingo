from typing import List

from .Examples import Responses as Examples
from ..Attributes import ModelId, ClassDetection, DocumentsId, DocumentId, DocumentModel


class Classify(Examples.Classify):
    classes: List[ClassDetection]


class CreateModel(ModelId):
    pass


class CreateDocuments(Examples.CreateDocuments, DocumentsId):
    pass


class DeleteDocument(Examples.DeleteDocument, DocumentId):
    pass


class TrainModel(Examples.TrainModel, ModelId):
    pass


class DeployModel(Examples.DeployModel, ModelId):
    pass


class ClearModel(Examples.ClearModel, ModelId):
    pass


class DeleteModel(Examples.DeleteModel, ModelId):
    pass


class UpdateDocument(Examples.UpdateDocument, DocumentId):
    pass


class ListDocuments(Examples.ListDocuments):
    documents: List[DocumentModel]
