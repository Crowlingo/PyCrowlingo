from typing import List

from .Examples import Responses as Examples
from ..Attributes import QuestionId, AnswerId, QuestionsId, AnswersId, QuestionModel, \
    AnswerModel, FaqSearchResult


class Search(Examples.Search):
    results: List[FaqSearchResult]


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
