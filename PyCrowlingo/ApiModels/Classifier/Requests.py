from typing import List, Optional

from . import Responses
from .Examples import Requests as Examples
from ..Attributes import ModelId, Document, DocumentId, ProdVersion, CustomDocument, Text, Lang, \
    ID_TYPE, ClassId, Pagination, Id, ModelOwner, OptionalFeatures
from ..Basic import BasicModel


class Base(BasicModel):
    _prefix = "/classifier"
    _response_module = Responses
    _price = 0


class Classify(Examples.Classify, Base, Document, OptionalFeatures):
    _endpoint = "{model_id}/classify"
    _price = 1
    _responses = [400, 404]

    class Query(ModelId, ModelOwner, ProdVersion):
        pass


class CreateDocuments(Examples.CreateDocuments, Base):
    _endpoint = "{model_id}/documents/"
    _responses = [403, 404, 409, 411, 413]
    documents: List[CustomDocument]

    class Query(ModelId, ModelOwner):
        pass


class DeleteDocument(Examples.DeleteDocument, Base):
    _endpoint = "{model_id}/documents/{document_id}"
    _method = "DELETE"
    _responses = [403, 404]

    class Query(ModelId, ModelOwner, DocumentId):
        pass


class UpdateDocument(Examples.UpdateDocument, Base, Lang, Text):
    _endpoint = "{model_id}/documents/{document_id}"
    _method = "PATCH"
    _responses = [403, 404, 411, 413]

    class_id: Optional[ID_TYPE] = None

    class Query(ModelId, ModelOwner, DocumentId):
        pass


class GetDocument(Examples.GetDocument, Base):
    _endpoint = "{model_id}/documents/{document_id}"
    _method = "GET"
    _responses = [404]

    class Query(ModelId, ModelOwner, DocumentId):
        pass


class ListDocuments(Examples.ListDocuments, Base):
    _endpoint = "{model_id}/documents/"
    _method = "GET"
    _responses = [404]

    class Query(ModelId, ModelOwner, Id, Lang, ClassId, Pagination):
        pass
