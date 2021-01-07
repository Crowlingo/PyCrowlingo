from pydantic import BaseModel


class Extract(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                'concepts': [{'properties': None,
                              'labels': [{'mentions': [{'start': 57, 'end': 67}], 'text': 'Mar a Lago'}],
                              'weight': 0.14802610884279066, 'id': 'Q1262898'},
                             {'properties': None,
                              'labels': [{'mentions': [{'start': 149, 'end': 160},
                                                       {'start': 227, 'end': 238}], 'text': 'impeachment'}],
                              'weight': 0.1254129262256732, 'id': 'Q480498'},
                             {'properties': None,
                              'labels': [{'mentions': [{'start': 322, 'end': 329}], 'text': 'Ukraine'}],
                              'weight': 0.11488780170151257, 'id': 'Q212'},
                             {'properties': None,
                              'labels': [{'mentions': [{'start': 78, 'end': 85}], 'text': 'Florida'}],
                              'weight': 0.08954558607148629, 'id': 'Q812'},
                             {'properties': None,
                              'labels': [{'mentions': [{'start': 25, 'end': 29}], 'text': 'golf'}],
                              'weight': 0.07830946680736198, 'id': 'Q5377'},
                             {'properties': None,
                              'labels': [{'mentions': [{'start': 279, 'end': 287}], 'text': 'Congress'}],
                              'weight': 0.07515613559680595, 'id': 'Q11268'},
                             {'properties': None,
                              'labels': [{'mentions': [{'start': 177, 'end': 187}], 'text': 'Democratic'}],
                              'weight': 0.0734013547521301, 'id': 'Q29552'},
                             {'properties': None,
                              'labels': [{'mentions': [{'start': 0, 'end': 5}], 'text': 'Trump'}],
                              'weight': 0.07132417397214992, 'id': 'Q22686'},
                             {'properties': None,
                              'labels': [{'mentions': [{'start': 298, 'end': 309}], 'text': 'President s'}],
                              'weight': 0.06936923906991745, 'id': 'Q11696'},
                             {'properties': None,
                              'labels': [{'mentions': [{'start': 334, 'end': 343}], 'text': 'political'}],
                              'weight': 0.059373008941530046, 'id': 'Q7163'},
                             {'properties': None,
                              'labels': [
                                  {'mentions': [{'start': 215, 'end': 238}], 'text': 'articles of impeachment'}],
                              'weight': 0.05072255562179739, 'id': 'Q1949797'},
                             {'properties': None,
                              'labels': [{'mentions': [{'start': 257, 'end': 262}], 'text': 'power'}],
                              'weight': 0.04447164239684429, 'id': 'Q25107'}
                             ]
            }
        }


class ExtractCustom(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                'concepts': [{'properties': None,
                              'labels': [{'mentions': [{'start': 0, 'end': 4, 'similarity': 0.8119}], 'text': 'Hello'}],
                              'id': 'Greeting'},
                             ]
            }
        }

class CreateConcepts(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                "concepts_id": ["Greeting"]
            }
        }


class CreateLabels(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                "labels_id": ["aiJ4gtGm"]
            }
        }


class DeleteConcept(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                "concept_id": "Greeting"
            }

        }


class DeleteLabel(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                "label_id": "aiJ4gtGm"
            }
        }


class UpdateConcept(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                "concept_id": "Greeting"
            }
        }


class UpdateLabel(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                "label_id": "aiJ4gtGm"
            }
        }


class GetLabel(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                "text": "Bonjour", "lang": "fr", "concept_id": "Greeting"
            }
        }


class GetConcept(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                "id": "Greeting", "properties": {}
            }
        }


class ListLabels(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                "labels": [{"text": "Bonjour", "lang": "fr", "concept_id": "Greeting"}]
            }
        }


class ListConcepts(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                "concepts": [{"id": "Greeting", "properties": {}}]
            }
        }
