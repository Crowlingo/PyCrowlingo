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


class CreateDocuments(BaseModel):
    class Config:
        _model_id = "AskUbuntu"
        _documents = [{
            "text": "How to setup wireless printing from a printer connected via usb on Ubuntu Server 12.10?",
            "class_id": "Setup Printer"
        }]

        schema_extra = {
            "example": {
                "documents": _documents
            },
            "_python": [f"model_id = \"{_model_id}\"", f"documents = \"{_documents}\"",
                        "client.classifier.create_documents(model_id, documents)"]
        }


class DeleteDocument(BaseModel):
    class Config:
        _model_id = "AskUbuntu"
        _sentence_id = "PQk4AQbu"
        schema_extra = {
            "_python": [f"model_id = \"{_model_id}\"", f"sentence_id = \"{_sentence_id}\"",
                        "client.classifier.delete_document(model_id, sentence_id)"]
        }


class UpdateDocument(BaseModel):
    class Config:
        _model_id = "AskUbuntu"
        _class_id = "Software Recommendation"
        _document_id = "PQk4AQbu"
        schema_extra = {
            "example": {
                "class_id": _class_id
            },
            "_python": [f"model_id = \"{_model_id}\"", f"document_id = \"{_document_id}\"",
                        f"class_id = \"{_class_id}\"",
                        "client.classifier.update_document(model_id, document_id, class_id=class_id)"]
        }


class GetDocument(BaseModel):
    class Config:
        _model_id = "AskUbuntu"
        _document_id = "PQk4AQbu"
        schema_extra = {
            "_python": [f"model_id = \"{_model_id}\"", f"document_id = \"{_document_id}\""
                        "client.classifier.get_document(model_id, document_id)"]
        }


class ListDocuments(BaseModel):
    class Config:
        _model_id = "AskUbuntu"
        schema_extra = {
            "_python": [f"model_id = \"{_model_id}\"",
                        "client.classifier.list_documents(model_id)"]
        }


class RenameClass(BaseModel):
    class Config:
        _model_id = "AskUbuntu"
        _old_class_id = "Out Of Scope"
        _new_class_id = "OOS"
        schema_extra = {
            "_python": [f"model_id = \"{_model_id}\"",
                        f"old_class_id= \"{_old_class_id}\"",
                        f"new_class_id= \"{_new_class_id}\"",
                        "client.classifier.rename_class(model_id, old_class_id, new_class_id)"]
        }
