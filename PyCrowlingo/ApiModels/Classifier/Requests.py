from . import Responses
from .Examples import Requests as Examples
from ..Attributes import ModelId, Document, ClassId, Id, SentenceId
from ..Basic import BasicModel


class Base(BasicModel):
    _prefix = "/classifier"
    _response_module = Responses
    _price = 0


class Classify(Examples.Classify, Base, Document):
    _endpoint = "{model_id}/classify"
    _price = 1

    class Query(ModelId):
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


class DeleteModel(Examples.DeleteModel, Base):
    _endpoint = "{model_id}"
    _method = "DELETE"

    class Query(ModelId):
        pass


class CreateSentence(Examples.CreateSentence, Base, Id, Document):
    _endpoint = "{model_id}/class/{class_id}/sentences/"

    class Query(ModelId, ClassId):
        pass


class DeleteSentence(Examples.DeleteSentence, Base):
    _endpoint = "{model_id}/sentences/{sentence_id}"
    _method = "DELETE"

    class Query(ModelId, SentenceId):
        pass
