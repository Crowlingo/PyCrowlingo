from pydantic import BaseModel


class Get(BaseModel):
    class Config:
        _model_id = "AskUbuntu"
        schema_extra = {
            "_python": [f"model_id = \"{_model_id}\"",
                        "client.model.get(model_id)"]
        }


class Create(BaseModel):
    class Config:
        _model_id = "AskUbuntu"
        _category = "classifier"
        schema_extra = {
            "_python": [f"model_id = \"{_model_id}\"", f"category = \"{_category}\""
                        "client.model.create(model_id, category)"]
        }


class Train(BaseModel):
    class Config:
        _model_id = "AskUbuntu"
        schema_extra = {
            "_python": [f"model_id = \"{_model_id}\"",
                        "client.model.train(model_id)"]
        }


class Deploy(BaseModel):
    class Config:
        _model_id = "AskUbuntu"
        schema_extra = {
            "_python": [f"model_id = \"{_model_id}\"",
                        "client.model.deploy(model_id)"]
        }


class Clear(BaseModel):
    class Config:
        _model_id = "AskUbuntu"
        schema_extra = {
            "_python": [f"model_id = \"{_model_id}\"",
                        "client.model.clear(model_id)"]
        }


class Delete(BaseModel):
    class Config:
        _model_id = "AskUbuntu"
        schema_extra = {
            "_python": [f"model_id = \"{_model_id}\"",
                        "client.model.delete(model_id)"]
        }


class AddCollaborator(BaseModel):
    class Config:
        _model_id = "AskUbuntu"
        schema_extra = {
            "_python": [f"model_id = \"{_model_id}\"",
                        f"email = \"john@crowlingo.com\"",
                        "client.model.add_collaborator(model_id, email)"]
        }


class RemoveCollaborator(BaseModel):
    class Config:
        _model_id = "AskUbuntu"
        schema_extra = {
            "_python": [f"model_id = \"{_model_id}\"",
                        f"email = \"john@crowlingo.com\"",
                        "client.model.remove_collaborator(model_id, email)"]
        }


class Edit(BaseModel):
    class Config:
        _model_id = "AskUbuntu"
        _description = "Best model ever"
        schema_extra = {
            "_python": [f"model_id = \"{_model_id}\"",
                        f"description = \"{_description}\"",
                        "client.model.edit(model_id, description=description)"]
        }


class ListPublic(BaseModel):
    class Config:
        schema_extra = {
            "_python": ["client.model.list_public()"]
        }


class ListUser(BaseModel):
    class Config:
        schema_extra = {
            "_python": ["client.model.list_user()"]
        }
