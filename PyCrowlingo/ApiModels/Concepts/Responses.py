from .Examples import Responses as Examples
from ..Attributes import Concepts, ConceptId, LabelId, ModelId


class Extract(Examples.Extract, Concepts):
    pass


class TrainModel(Examples.TrainModel, ModelId):
    pass


class CreateModel(Examples.CreateModel, ModelId):
    pass


class CreateConcept(Examples.CreateConcept, ConceptId):
    pass


class CreateLabel(Examples.CreateLabel, LabelId):
    pass


class DeleteModel(Examples.DeleteModel, ModelId):
    pass


class DeleteLabel(Examples.DeleteLabel, LabelId):
    pass


class DeleteConcept(Examples.DeleteConcept, ConceptId):
    pass
