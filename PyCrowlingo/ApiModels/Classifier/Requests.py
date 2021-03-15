from typing import List, Optional

from . import Responses
from .Examples import Requests as Examples
from ..Attributes import ModelId, Document, DocumentId, ProdVersion, CustomDocument, Text, Lang, \
    ID_TYPE, ClassId, Pagination, Id, OptionalFeatures, OldClassId, NewClassId, Markers, Marker, Upsert
from ..Basic import BasicModel


class Base(BasicModel):
    _prefix = "/classifier"
    _response_module = Responses
    _price = 0


class Classify(Examples.Classify, Base, Document, OptionalFeatures):
    _endpoint = "{model_id}/classify"
    _price = 1
    _responses = [400, 404]

    class Query(ModelId, ProdVersion):
        pass


class CreateDocuments(Examples.CreateDocuments, Base, Upsert):
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


class UpdateDocument(Examples.UpdateDocument, Base, Lang, Text, Markers):
    _endpoint = "{model_id}/documents/{document_id}"
    _method = "PATCH"
    _responses = [403, 404, 411, 413]

    class_id: Optional[ID_TYPE] = None

    class Query(ModelId, DocumentId):
        pass


class GetDocument(Examples.GetDocument, Base):
    _endpoint = "{model_id}/documents/{document_id}"
    _method = "GET"
    _responses = [403, 404]

    class Query(ModelId, DocumentId):
        pass


class ListDocuments(Examples.ListDocuments, Base):
    _endpoint = "{model_id}/documents/"
    _method = "GET"
    _responses = [403, 404]

    class Query(ModelId, Id, Lang, ClassId, Pagination, Marker):
        pass


class RenameClass(Examples.RenameClass, Base):
    _endpoint = "{model_id}/classes/{old_class_id}"
    _method = "PATCH"
    _responses = [403, 404]

    class Query(ModelId, OldClassId, NewClassId):
        pass
