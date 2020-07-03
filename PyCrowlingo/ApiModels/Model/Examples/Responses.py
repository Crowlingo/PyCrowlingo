from pydantic import BaseModel


class Get(BaseModel):
    class Config:
        schema_extra = {
            "example":
                {"name": "AskUbuntu",
                 "category": "classifier",
                 "training_status": "done",
                 "owner": "john@crowlingo.com",
                 "deployed": True,
                 "metrics": {},
                 "collaborators": {}}
        }



class Train(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                "model_id": "AskUbuntu"
            }
        }


class Deploy(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                "model_id": "AskUbuntu"
            }
        }


class Clear(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                "model_id": "AskUbuntu"
            }
        }


class Delete(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                "model_id": "AskUbuntu"
            }
        }


class AddCollaborator(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                "collaborator": "john@crowlingo.com"
            }
        }


class RemoveCollaborator(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                "collaborator": "john@crowlingo.com"
            }
        }
