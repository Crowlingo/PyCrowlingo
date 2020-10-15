from typing import List, Dict

from . import Responses
from .Examples import Requests as Examples
from ..Attributes import ModelId, QuestionId, AnswerId, Document, ProdVersion, CustomQuestion, \
    CustomAnswer, ID_TYPE, Pagination, Id, ModelOwner
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

    class Query(ModelId, ModelOwner, ProdVersion):
        limit: int = 1


class CreateQuestions(Examples.CreateQuestions, Base):
    _endpoint = "{model_id}/questions"
    _responses = [403, 404, 409, 411, 413]
    questions: List[CustomQuestion]

    class Query(ModelId, ModelOwner):
        pass


class CreateAnswers(Examples.CreateAnswers, Base):
    _endpoint = "{model_id}/answers"
    _responses = [403, 404, 409, 411, 413]
    answers: List[CustomAnswer]

    class Query(ModelId, ModelOwner):
        pass


class DeleteQuestion(Examples.DeleteQuestion, Base):
    _endpoint = "{model_id}/questions/{question_id}"
    _method = "DELETE"
    _responses = [403, 404]

    class Query(ModelId, ModelOwner, QuestionId):
        pass


class DeleteAnswer(Examples.DeleteAnswer, Base):
    _endpoint = "{model_id}/answers/{answer_id}"
    _method = "DELETE"
    _responses = [403, 404]

    class Query(ModelId, ModelOwner, AnswerId):
        pass


class UpdateQuestion(Examples.UpdateQuestion, Base, AnswerId):
    _endpoint = "{model_id}/questions/{question_id}"
    _method = "PATCH"
    _responses = [403, 404, 411, 413]
    variations: Dict[ID_TYPE, str] = None

    class Query(ModelId, ModelOwner, QuestionId):
        pass


class UpdateAnswer(Examples.UpdateAnswer, Base):
    _endpoint = "{model_id}/answers/{answer_id}"
    _method = "PATCH"
    _responses = [403, 404, 411, 413]
    variations: Dict[ID_TYPE, str] = None

    class Query(ModelId, ModelOwner, AnswerId):
        pass


class GetQuestion(Examples.GetQuestion, Base):
    _endpoint = "{model_id}/questions/{question_id}"
    _method = "GET"
    _responses = [404]

    class Query(ModelId, ModelOwner, QuestionId):
        pass


class GetAnswer(Examples.GetAnswer, Base):
    _endpoint = "{model_id}/answers/{answer_id}"
    _method = "GET"
    _responses = [404]

    class Query(ModelId, ModelOwner, AnswerId):
        pass


class ListQuestions(Examples.ListQuestions, Base):
    _endpoint = "{model_id}/questions/"
    _method = "GET"
    _responses = [404]

    class Query(ModelId, ModelOwner, Id, AnswerId, Pagination):
        pass


class ListAnswers(Examples.ListAnswers, Base):
    _endpoint = "{model_id}/answers/"
    _method = "GET"
    _responses = [404]

    class Query(ModelId, ModelOwner, Id, Pagination):
        pass
