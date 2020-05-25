from . import Responses
from .Examples import Requests as Examples
from ..Attributes import Precision, Split, ModelId, Properties, Document, ConceptId, LabelId, Id
from ..Basic import BasicModel


class Base(BasicModel):
    _prefix = "/concepts"
    _response_module = Responses
    _price = 0


class Extract(Examples.Extract, Base, Document, Properties):
    _price = 1

    class Query(Precision, Split, ModelId):
        pass


class TrainModel(Examples.TrainModel, Base):
    _endpoint = "{model_id}/train"
    _price = 1

    class Query(ModelId):
        pass


class CreateModel(Examples.CreateModel, Base):
    _endpoint = "{model_id}/create"

    class Query(ModelId):
        pass


class CreateConcept(Examples.CreateConcept, Base, Id, Properties):
    _endpoint = "{model_id}/concepts"

    class Query(ModelId):
        pass


class CreateLabel(Examples.CreateLabel, Base, Id, ConceptId, Document):
    _endpoint = "{model_id}/labels"
    precision: float = 0.75

    class Query(ModelId):
        pass


class DeleteModel(Examples.DeleteModel, Base):
    _endpoint = "{model_id}"
    _method = "DELETE"

    class Query(ModelId):
        pass


class DeleteConcept(Examples.DeleteConcept, Base):
    _endpoint = "{model_id}/concepts/{concept_id}"
    _method = "DELETE"

    class Query(ModelId, ConceptId):
        pass


class DeleteLabel(Examples.DeleteLabel, Base):
    _endpoint = "{model_id}/labels/{label_id}"
    _method = "DELETE"

    class Query(ModelId, LabelId):
        pass
