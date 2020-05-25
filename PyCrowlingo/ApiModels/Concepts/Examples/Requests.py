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


class CreateModel(BaseModel):
    class Config:
        _model_id = "my_model"
        schema_extra = {
            "_python": [f"model_id = \"{_model_id}\"",
                        "client.concepts.create_model(model_id)"]
        }


class CreateConcept(BaseModel):
    class Config:
        _model_id = "my_model"
        _id = "Greeting"
        schema_extra = {
            "example": {
                "id": _id
            },
            "_python": [f"model_id = \"{_model_id}\"", f"id = \"{_id}\"",
                        "client.concepts.create_concept(model_id, id)"]
        }


class CreateLabel(BaseModel):
    class Config:
        _model_id = "my_model"
        _text = "Bonjour"
        _concept_id = "Greeting"
        schema_extra = {
            "example": {
                "text": _text,
                "concept_id": _concept_id
            },
            "_python": [f"model_id = \"{_model_id}\"", f"text = \"{_text}\"", f"concept_id = \"{_concept_id}\"",
                        "client.concepts.create_label(model_id, text, concept_id=concept_id)"]
        }


class DeleteModel(BaseModel):
    class Config:
        _model_id = "my_model"
        schema_extra = {
            "_python": [f"model_id = \"{_model_id}\"",
                        "client.concepts.delete_model(model_id)"]
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


class TrainModel(BaseModel):
    class Config:
        _model_id = "my_model"
        schema_extra = {
            "_python": [f"model_id = \"{_model_id}\"",
                        "client.concepts.train_model(model_id)"]
        }
