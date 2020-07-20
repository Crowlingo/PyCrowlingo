from typing import List

from .Examples import Responses as Examples
from ..Attributes import Concepts, ConceptId, LabelId, ConceptsId, LabelsId, LabelModel, ConceptModel, CustomConceptRes


class Extract(Examples.Extract, Concepts):
    pass


class ExtractCustom(Examples.ExtractCustom):
    concepts: List[CustomConceptRes]


class CreateConcepts(Examples.CreateConcepts, ConceptsId):
    pass


class CreateLabels(Examples.CreateLabels, LabelsId):
    pass


class UpdateConcept(Examples.UpdateConcept, ConceptId):
    pass


class UpdateLabel(Examples.UpdateLabel, LabelId):
    pass


class DeleteLabel(Examples.DeleteLabel, LabelId):
    pass


class DeleteConcept(Examples.DeleteConcept, ConceptId):
    pass


class GetLabel(Examples.GetLabel, LabelModel):
    pass


class GetConcept(Examples.GetConcept, ConceptModel):
    pass


class ListLabels(Examples.ListLabels):
    labels: List[LabelModel]


class ListConcepts(Examples.ListConcepts):
    concepts: List[ConceptModel]
