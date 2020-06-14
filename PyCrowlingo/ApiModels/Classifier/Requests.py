from typing import List, Optional

from . import Responses
from .Examples import Requests as Examples
from ..Attributes import ModelId, Document, DocumentId, ProdVersion, ModelType, CustomDocument, Text, Lang, \
    ID_TYPE, ClassId, Pagination, Id
from ..Basic import BasicModel


class Base(BasicModel):
    _prefix = "/classifier"
    _response_module = Responses
    _price = 0


class Classify(Examples.Classify, Base, Document):
    _endpoint = "{model_id}/classify"
    _price = 1
    _responses = [400, 404]

    class Query(ModelId, ProdVersion):
        pass


class TrainModel(Examples.TrainModel, Base):
    _endpoint = "{model_id}/train"
    _price = 1
    _responses = [403, 404]

    class Query(ModelId):
        model_type: ModelType = ModelType.SVM


class CreateModel(Examples.CreateModel, Base):
    _endpoint = "{model_id}/create"
    _responses = [403, 409]

    class Query(ModelId):
        pass


class DeleteModel(Examples.DeleteModel, Base):
    _endpoint = "{model_id}"
    _method = "DELETE"
    _responses = [403, 404]

    class Query(ModelId):
        pass


class DeployModel(Examples.DeployModel, Base):
    _endpoint = "{model_id}/deploy"
    _responses = [403, 404]

    class Query(ModelId):
        pass


class ClearModel(Examples.ClearModel, Base):
    _endpoint = "{model_id}/clear"
    _responses = [403, 404]

    class Query(ModelId):
        pass


class CreateDocuments(Examples.CreateDocuments, Base):
    _endpoint = "{model_id}/documents/"
    _responses = [403, 404, 409, 411, 413]
    documents: List[CustomDocument]

    class Query(ModelId):
        pass


class DeleteDocument(Examples.DeleteDocument, Base):
    _endpoint = "{model_id}/documents/{document_id}"
    _method = "DELETE"
    _responses = [403, 404]

    class Query(ModelId, DocumentId):
        pass


class UpdateDocument(Examples.UpdateDocument, Base, Lang, Text):
    _endpoint = "{model_id}/documents/{document_id}"
    _method = "PATCH"
    _responses = [403, 404, 411, 413]

    class_id: Optional[ID_TYPE] = None

    class Query(ModelId, DocumentId):
        pass


class ListDocuments(Examples.UpdateDocument, Base):
    _endpoint = "{model_id}/documents/"
    _method = "GET"
    _responses = [403, 404]

    class Query(ModelId, Id, Lang, ClassId, Pagination):
        pass
