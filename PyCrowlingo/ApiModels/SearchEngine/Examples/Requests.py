from pydantic import BaseModel


class Search(BaseModel):
    class Config:
        _model_id = "search_newspaper"
        _text = 'attack'
        schema_extra = {
            "example": {
                "text": _text
            },
            "_python": [f"model_id = \"{_model_id}\"", f"text = \"{_text}\"",
                        "client.search_engine.search(model_id, text)"]
        }


class CreateDocuments(BaseModel):
    class Config:
        _model_id = "search_newspaper"
        _documents = [{"text": "Crowlingo provides NLP services to find insights and relationships in text of 100+ "
                               "different languages."}]
        schema_extra = {
            "example": {
                "documents": _documents
            },
            "_python": [f"model_id = \"{_model_id}\"",
                        f"documents = {_documents}",
                        "client.search_engine.create_documents(model_id, documents)"]
        }


class CreateKeywords(BaseModel):
    class Config:
        _model_id = "search_newspaper"
        _keywords = [{"text": "Ministry of Foreign Affairs"}]
        schema_extra = {
            "example": {
                "keywords": _keywords
            },
            "_python": [f"model_id = \"{_model_id}\"",
                        f"keywords = {_keywords}",
                        "client.search_engine.create_keywords(model_id, keywords)"]
        }


class DeleteDocuments(BaseModel):
    class Config:
        _model_id = "search_newspaper"
        _documents_id = ["jLcbfzso"]
        schema_extra = {
            "example": {
                "documents_id": _documents_id
            },
            "_python": [f"model_id = \"{_model_id}\"",
                        f"documents_id = {_documents_id}",
                        "client.search_engine.delete_documents(model_id, documents_id)"]
        }
