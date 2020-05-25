from typing import List

from .Examples import Responses as Examples
from ..Attributes import ModelId, ClassDetection


class Classify(Examples.Classify):
    classes: List[ClassDetection]


class CreateModel(ModelId):
    pass


class CreateSentence(Examples.CreateSentence):
    sentence_id: str


class DeleteSentence(Examples.DeleteSentence):
    sentence_id: str


class TrainModel(Examples.TrainModel, ModelId):
    pass


class DeleteModel(Examples.DeleteModel, ModelId):
    pass
