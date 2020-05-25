from typing import Optional

from .Examples import Responses as Examples
from ..Attributes import Answer, Question, QuestionId, AnswerId, ModelId


class Search(Examples.Search):
    question: Optional[Question]
    answer: Optional[Answer]
    similarity: Optional[float]


class TrainModel(ModelId):
    pass


class CreateModel(ModelId):
    pass


class CreateQuestion(QuestionId):
    pass


class CreateAnswer(AnswerId):
    pass


class DeleteModel(ModelId):
    pass


class DeleteQuestion(QuestionId):
    pass


class DeleteAnswer(AnswerId):
    pass
