from typing import List

from .Examples import Responses as Examples
from ..Attributes import Concepts, ConceptId, LabelId, ModelId, ConceptsId, LabelsId, LabelModel, ConceptModel


class Extract(Examples.Extract, Concepts):
    pass


class TrainModel(Examples.TrainModel, ModelId):
    pass


class DeployModel(Examples.DeployModel, ModelId):
    pass


class ClearModel(Examples.ClearModel, ModelId):
    pass


class CreateModel(Examples.CreateModel, ModelId):
    pass


class CreateConcepts(Examples.CreateConcepts, ConceptsId):
    pass


class CreateLabels(Examples.CreateLabels, LabelsId):
    pass


class UpdateConcept(Examples.UpdateConcept, ConceptId):
    pass


class UpdateLabel(Examples.UpdateLabel, LabelId):
    pass


class DeleteModel(Examples.DeleteModel, ModelId):
    pass


class DeleteLabel(Examples.DeleteLabel, LabelId):
    pass


class DeleteConcept(Examples.DeleteConcept, ConceptId):
    pass


class ListLabels(Examples.ListLabels):
    labels: List[LabelModel]


class ListConcepts(Examples.ListConcepts):
    concepts: List[ConceptModel]
