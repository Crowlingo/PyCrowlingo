from typing import Optional, List

from .Examples import Responses as Examples
from ..Attributes import Answer, Question, QuestionId, AnswerId, ModelId, QuestionsId, AnswersId, QuestionModel, \
    AnswerModel


class Search(Examples.Search):
    question: Optional[Question]
    answer: Optional[Answer]
    similarity: Optional[float]


class TrainModel(Examples.TrainModel, ModelId):
    pass


class DeployModel(Examples.DeployModel, ModelId):
    pass


class CreateModel(Examples.CreateModel, ModelId):
    pass


class ClearModel(Examples.ClearModel, ModelId):
    pass


class CreateQuestions(Examples.CreateQuestions, QuestionsId):
    pass


class CreateAnswers(Examples.CreateAnswers, AnswersId):
    pass


class UpdateQuestion(Examples.UpdateQuestion, QuestionId):
    pass


class UpdateAnswer(Examples.UpdateAnswer, AnswerId):
    pass


class DeleteModel(Examples.DeleteModel, ModelId):
    pass


class DeleteQuestion(Examples.DeleteQuestion, QuestionId):
    pass


class DeleteAnswer(Examples.DeleteAnswer, AnswerId):
    pass


class ListQuestions(Examples.ListQuestions):
    questions: List[QuestionModel]


class ListAnswers(Examples.ListAnswers):
    answers: List[AnswerModel]
