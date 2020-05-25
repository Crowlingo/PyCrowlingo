from pydantic import BaseModel


class Classify(BaseModel):
    class Config:
        _model_id = "AskUbuntu"
        _text = "Est-il recommandé d'utiliser MongoDb pour indexer mes documents ?"
        schema_extra = {
            "example": {
                "text": _text
            },
            "_python": [f"model_id = \"{_model_id}\"", f"text = \"{_text}\"",
                        "client.classifier.classify(model_id, text)"]
        }


class CreateSentence(BaseModel):
    class Config:
        _model_id = "AskUbuntu"
        _text = "How to setup wireless printing from a printer connected via usb on Ubuntu Server 12.10?"
        _class_id = "Setup Printer"

        schema_extra = {
            "example": {
                "text": _text
            },
            "_python": [f"model_id = \"{_model_id}\"", f"text = \"{_text}\"", f"class_id = \"{_class_id}\"",
                        "client.classifier.create_sentence(model_id, text, class_id)"]
        }


class DeleteSentence(BaseModel):
    class Config:
        _model_id = "AskUbuntu"
        _sentence_id = "PQk4AQbu"
        schema_extra = {
            "_python": [f"model_id = \"{_model_id}\"", f"sentence_id = \"{_sentence_id}\"",
                        "client.classifier.delete_sentence(model_id, sentence_id)"]
        }


class CreateModel(BaseModel):
    class Config:
        _model_id = "AskUbuntu"
        schema_extra = {
            "_python": [f"model_id = \"{_model_id}\"",
                        "client.classifier.create_model(model_id)"]
        }


class TrainModel(BaseModel):
    class Config:
        _model_id = "AskUbuntu"
        schema_extra = {
            "_python": [f"model_id = \"{_model_id}\"",
                        "client.classifier.train_model(model_id)"]
        }


class DeleteModel(BaseModel):
    class Config:
        _model_id = "AskUbuntu"
        schema_extra = {
            "_python": [f"model_id = \"{_model_id}\"",
                        "client.classifier.delete_model(model_id)"]
        }
