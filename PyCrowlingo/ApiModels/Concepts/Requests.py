from typing import List, Dict

from . import Responses
from .Examples import Requests as Examples
from ..Attributes import Precision, Split, ModelId, Properties, Document, ConceptId, LabelId, ProdVersion, \
    CustomConcept, CustomLabel, Text, Lang, Pagination, Id, Markers, Marker, Upsert
from ..Basic import BasicModel


class Base(BasicModel):
    _prefix = "/concepts"
    _response_module = Responses
    _price = 0


class Extract(Examples.Extract, Base, Document, Properties):
    _price = 1
    _responses = [400, 404]

    class Query(Precision, Split):
        pass


class ExtractCustom(Examples.ExtractCustom, Base, Document, Properties):
    _price = 1
    _responses = [400, 404]

    class Query(ModelId, ProdVersion):
        pass


class CreateConcepts(Examples.CreateConcepts, Base, Upsert):
    _endpoint = "{model_id}/concepts"
    _responses = [403, 404, 409, 411, 413]
    concepts: List[CustomConcept]

    class Query(ModelId):
        pass


class CreateLabels(Examples.CreateLabels, Base, Upsert):
    _endpoint = "{model_id}/labels"
    _responses = [403, 404, 409, 411, 413]
    labels: List[CustomLabel]

    class Query(ModelId):
        pass


class DeleteConcept(Examples.DeleteConcept, Base):
    _endpoint = "{model_id}/concepts/{concept_id}"
    _method = "DELETE"
    _responses = [403, 404]

    class Query(ModelId, ConceptId):
        pass


class DeleteLabel(Examples.DeleteLabel, Base):
    _endpoint = "{model_id}/labels/{label_id}"
    _method = "DELETE"
    _responses = [403, 404]

    class Query(ModelId, LabelId):
        pass


class UpdateConcept(Examples.UpdateConcept, Base, Markers):
    _endpoint = "{model_id}/concepts/{concept_id}"
    _method = "PATCH"
    _responses = [403, 404, 411, 413]
    properties: Dict[str, str] = None

    class Query(ModelId, ConceptId):
        pass


class UpdateLabel(Examples.UpdateLabel, Base, Text, Lang, ConceptId, Markers):
    _endpoint = "{model_id}/labels/{label_id}"
    _method = "PATCH"
    _responses = [403, 404, 411, 413]

    class Query(ModelId, LabelId):
        pass


class GetLabel(Examples.GetLabel, Base):
    _endpoint = "{model_id}/labels/{label_id}"
    _method = "GET"
    _responses = [404]

    class Query(ModelId, LabelId):
        pass


class GetConcept(Examples.GetConcept, Base):
    _endpoint = "{model_id}/concepts/{concept_id}"
    _method = "GET"
    _responses = [404]

    class Query(ModelId, ConceptId):
        pass


class ListLabels(Examples.ListLabels, Base):
    _endpoint = "{model_id}/labels"
    _method = "GET"
    _responses = [404]

    class Query(ModelId, Id, Lang, ConceptId, Text, Pagination, Marker):
        pass


class ListConcepts(Examples.ListConcepts, Base):
    _endpoint = "{model_id}/concepts"
    _method = "GET"
    _responses = [404]

    class Query(ModelId, Id, Pagination, Marker):
        pass
