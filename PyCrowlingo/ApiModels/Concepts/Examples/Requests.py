from pydantic import BaseModel


class Extract(BaseModel):
    class Config:
        _text = "On 26 April 1986, Chernobyl suffered the world’s worst nuclear disaster. An experiment designed to " \
                "test the safety of the power plant went wrong and caused a fire which spewed radiation for 10 days. " \
                "Clouds carrying radioactive particles drifted for thousands of miles, releasing toxic rain all over " \
                "Europe. Those living close to Chernobyl - about 116,000 people - were immediately evacuated. A 30 km " \
                "exclusion zone was imposed around the damaged reactor. This was later expanded to cover more " \
                "affected areas. "
        schema_extra = {
            "example": {
                "text": _text
            },
            "_python": [f"text = \"{_text}\"", "client.concepts.extract(text)"]
        }


class ExtractCustom(BaseModel):
    class Config:
        _text = "Hello my friend !"
        _model_id = "my_model"
        schema_extra = {
            "example": {
                "text": _text
            },
            "_python": [f"model_id = \"{_model_id}\"", f"text = \"{_text}\"",
                        "client.concepts.extract_custom(my_model, text)"]
        }


class CreateConcepts(BaseModel):
    class Config:
        _model_id = "my_model"
        _concepts = [{"id": "Greeting"}]
        schema_extra = {
            "example": {
                "concepts": _concepts
            },
            "_python": [f"model_id = \"{_model_id}\"", f"concepts = \"{_concepts}\"",
                        "client.concepts.create_concepts(model_id, concepts)"]
        }


class CreateLabels(BaseModel):
    class Config:
        _model_id = "my_model"
        _labels = [{"text": "Bonjour", "concept_id": "Greeting"}]
        schema_extra = {
            "example": {
                "labels": _labels
            },
            "_python": [f"model_id = \"{_model_id}\"", f"labels = \"{_labels}\"",
                        "client.concepts.create_labels(model_id, labels)"]
        }


class DeleteConcept(BaseModel):
    class Config:
        _model_id = "my_model"
        _concept_id = "Greeting"
        schema_extra = {
            "_python": [f"model_id = \"{_model_id}\"", f"concept_id = \"{_concept_id}\"",
                        "client.concepts.delete_concept(model_id, concept_id)"]
        }


class DeleteLabel(BaseModel):
    class Config:
        _model_id = "my_model"
        _label_id = "aiJ4gtGm"
        schema_extra = {
            "_python": [f"model_id = \"{_model_id}\"", f"label_id = {_label_id}",
                        "client.concepts.delete_label(model_id, label_id)"]
        }


class UpdateConcept(BaseModel):
    class Config:
        _model_id = "my_model"
        _properties = {"title.en": "New Concept Title"}
        _concept_id = "Greeting"
        schema_extra = {
            "example": {
                "properties": _properties
            },
            "_python": [f"model_id = \"{_model_id}\"", f"concept_id = \"{_concept_id}\"",
                        f"properties = {_properties}",
                        "client.concepts.update_concept(model_id, concept_id, properties=properties)"]
        }


class UpdateLabel(BaseModel):
    class Config:
        _model_id = "my_model"
        _text = "Salut"
        _label_id = "aiJ4gtGm"
        schema_extra = {
            "example": {
                "text": _label_id
            },
            "_python": [f"model_id = \"{_model_id}\"", f"label_id = \"{_label_id}\"",
                        f"text = \"{_text}\"",
                        "client.concepts.update_label(model_id, label_id, text=text)"]
        }


class GetConcept(BaseModel):
    class Config:
        _model_id = "my_model"
        _concept_id = "Greeting"
        schema_extra = {
            "_python": [f"model_id = \"{_model_id}\"", f"concept_id = \"{_concept_id}\"",
                        "client.concepts.get_concept(model_id, concept_id)"]
        }


class GetLabel(BaseModel):
    class Config:
        _model_id = "my_model"
        _label_id = "aiJ4gtGm"
        schema_extra = {
            "_python": [f"model_id = \"{_model_id}\"", f"label_id = \"{_label_id}\"",
                        "client.concepts.get_label(model_id, label_id)"]
        }


class ListConcepts(BaseModel):
    class Config:
        _model_id = "my_model"
        schema_extra = {
            "_python": [f"model_id = \"{_model_id}\"",
                        "client.concepts.list_concepts(model_id)"]
        }


class ListLabels(BaseModel):
    class Config:
        _model_id = "my_model"
        schema_extra = {
            "_python": [f"model_id = \"{_model_id}\"",
                        "client.concepts.list_labels(model_id)"]
        }
