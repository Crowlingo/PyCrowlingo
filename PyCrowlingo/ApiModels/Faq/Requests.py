from typing import List

from . import Responses
from .Examples import Requests as Examples
from ..Attributes import ModelId, QuestionId, AnswerId, Document, Id, Variations
from ..Basic import BasicModel


class Base(BasicModel):
    _prefix = "/faq"
    _response_module = Responses
    _price = 0


class Search(Examples.Search, Base, Document):
    _endpoint = "{model_id}/search"
    _price = 1
    variations: List[str] = []  # try to pass it in query

    class Query(ModelId):
        pass


class TrainModel(Base):
    _endpoint = "{model_id}/train"
    _price = 1

    class Query(ModelId):
        pass


class CreateModel(Base):
    _endpoint = "{model_id}/create"

    class Query(ModelId):
        pass


class CreateQuestion(Examples.CreateQuestion, Base, Variations, Id, AnswerId):
    _endpoint = "{model_id}/questions"

    class Query(ModelId):
        pass


class CreateAnswer(Examples.CreateAnswer, Base, Variations, Id):
    _endpoint = "{model_id}/answers"

    class Query(ModelId):
        pass


class DeleteModel(Examples.DeleteModel, Base):
    _endpoint = "{model_id}"
    _method = "DELETE"

    class Query(ModelId):
        pass


class DeleteQuestion(Examples.DeleteQuestion, Base):
    _endpoint = "{model_id}/questions/{question_id}"
    _method = "DELETE"

    class Query(ModelId, QuestionId):
        pass


class DeleteAnswer(Examples.DeleteAnswer, Base):
    _endpoint = "{model_id}/answers/{answer_id}"
    _method = "DELETE"

    class Query(ModelId, AnswerId):
        pass
