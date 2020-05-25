from pydantic import BaseModel


class Classify(BaseModel):
    class Config:
        schema_extra = {
            "example":
                {'classes': [{'class_id': 'Software Recommendation', 'confidence': 0.6562462150850555},
                             {'class_id': 'None', 'confidence': 0.1208982732456724},
                             {'class_id': 'Shutdown Computer', 'confidence': 0.10488410138625179},
                             {'class_id': 'Setup Printer', 'confidence': 0.09517660221370582},
                             {'class_id': 'Make Update', 'confidence': 0.022794808069314842}]}
        }


class CreateSentence(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                "sentence_id": "PQk4AQbu"
            }
        }


class DeleteSentence(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                "sentence_id": "PQk4AQbu"
            }
        }


class TrainModel(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                "model_id": "AskUbuntu"
            }
        }


class DeleteModel(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                "model_id": "AskUbuntu"
            }
        }