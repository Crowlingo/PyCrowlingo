from typing import Optional, List

from .Examples import Responses as Examples
from ..Attributes import Answer, Question, QuestionId, AnswerId, QuestionsId, AnswersId, QuestionModel, \
    AnswerModel


class Search(Examples.Search):
    question: Optional[Question]
    answer: Optional[Answer]
    similarity: Optional[float]


class CreateQuestions(Examples.CreateQuestions, QuestionsId):
    pass


class CreateAnswers(Examples.CreateAnswers, AnswersId):
    pass


class UpdateQuestion(Examples.UpdateQuestion, QuestionId):
    pass


class UpdateAnswer(Examples.UpdateAnswer, AnswerId):
    pass


class DeleteQuestion(Examples.DeleteQuestion, QuestionId):
    pass


class DeleteAnswer(Examples.DeleteAnswer, AnswerId):
    pass


class GetQuestion(Examples.GetQuestion, QuestionModel):
    pass


class GetAnswer(Examples.GetAnswer, AnswerModel):
    pass


class ListQuestions(Examples.ListQuestions):
    questions: List[QuestionModel]


class ListAnswers(Examples.ListAnswers):
    answers: List[AnswerModel]
