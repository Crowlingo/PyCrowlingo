from typing import List, Dict

from . import Responses
from .Examples import Requests as Examples
from ..Attributes import ModelId, QuestionId, AnswerId, Document, ProdVersion, CustomQuestion, \
    CustomAnswer, ID_TYPE, Pagination, Id
from ..Basic import BasicModel


class Base(BasicModel):
    _prefix = "/faq"
    _response_module = Responses
    _price = 0


class Search(Examples.Search, Base, Document):
    _endpoint = "{model_id}/search"
    _price = 1
    _responses = [400, 404]
    variations: List[str] = []  # try to pass it in query

    class Query(ModelId, ProdVersion):
        pass


class TrainModel(Base):
    _endpoint = "{model_id}/train"
    _price = 1
    _responses = [403, 404]

    class Query(ModelId):
        pass


class DeployModel(Base):
    _endpoint = "{model_id}/deploy"
    _price = 1
    _responses = [403, 404]

    class Query(ModelId):
        pass


class ClearModel(Base):
    _endpoint = "{model_id}/clear"
    _price = 1
    _responses = [403, 404]

    class Query(ModelId):
        pass


class CreateModel(Base):
    _endpoint = "{model_id}/create"
    _responses = [403, 409]

    class Query(ModelId):
        pass


class CreateQuestions(Examples.CreateQuestions, Base):
    _endpoint = "{model_id}/questions"
    _responses = [403, 404, 409, 411, 413]
    questions: List[CustomQuestion]

    class Query(ModelId):
        pass


class CreateAnswers(Examples.CreateAnswers, Base):
    _endpoint = "{model_id}/answers"
    _responses = [403, 404, 409, 411, 413]
    answers: List[CustomAnswer]

    class Query(ModelId):
        pass


class DeleteModel(Examples.DeleteModel, Base):
    _endpoint = "{model_id}"
    _method = "DELETE"
    _responses = [403, 404]

    class Query(ModelId):
        pass


class DeleteQuestion(Examples.DeleteQuestion, Base):
    _endpoint = "{model_id}/questions/{question_id}"
    _method = "DELETE"
    _responses = [403, 404]

    class Query(ModelId, QuestionId):
        pass


class DeleteAnswer(Examples.DeleteAnswer, Base):
    _endpoint = "{model_id}/answers/{answer_id}"
    _method = "DELETE"
    _responses = [403, 404]

    class Query(ModelId, AnswerId):
        pass


class UpdateQuestion(Examples.UpdateQuestion, Base, AnswerId):
    _endpoint = "{model_id}/questions/{question_id}"
    _method = "PATCH"
    _responses = [403, 404, 411, 413]
    variations: Dict[ID_TYPE, str] = None

    class Query(ModelId, QuestionId):
        pass


class UpdateAnswer(Examples.UpdateAnswer, Base):
    _endpoint = "{model_id}/answers/{answer_id}"
    _method = "PATCH"
    _responses = [403, 404, 411, 413]
    variations: Dict[ID_TYPE, str] = None

    class Query(ModelId, AnswerId):
        pass


class ListQuestions(Examples.ListQuestions, Base):
    _endpoint = "{model_id}/questions/"
    _method = "GET"
    _responses = [403, 404]

    class Query(ModelId, Id, AnswerId, Pagination):
        pass


class ListAnswers(Examples.ListAnswers, Base):
    _endpoint = "{model_id}/answers/"
    _method = "GET"
    _responses = [403, 404]

    class Query(ModelId, Id, Pagination):
        pass
