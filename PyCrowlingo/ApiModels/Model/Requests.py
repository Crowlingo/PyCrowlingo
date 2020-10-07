from typing import Union

from . import Responses
from .Examples import Requests as Examples
from ..Attributes import ModelId, ModelType, ModelConfig, ModelOwner, Permissions, Email, Category, Metadata
from ..Basic import BasicModel


class Base(BasicModel):
    _prefix = "/models"
    _response_module = Responses
    _price = 0


class Get(Examples.Get, Base):
    _endpoint = "{model_id}"
    _method = "GET"
    _price = 0
    _responses = [404]

    class Query(ModelId, ModelOwner):
        pass


class Train(Examples.Train, Base, ModelConfig):
    _endpoint = "{model_id}/train"
    _price = 1
    _responses = [403, 404]

    class Query(ModelId, ModelOwner):
        model_type: Union[ModelType, str] = ModelType.SVM


class Create(Examples.Create, Base, Metadata):
    _endpoint = "{model_id}/create"
    _responses = [403, 409]

    class Query(ModelId):
        category: Category


class Delete(Examples.Delete, Base):
    _endpoint = "{model_id}"
    _method = "DELETE"
    _responses = [403, 404]

    class Query(ModelId, ModelOwner):
        pass


class Deploy(Examples.Deploy, Base):
    _endpoint = "{model_id}/deploy"
    _responses = [403, 404]

    class Query(ModelId, ModelOwner):
        pass


class Clear(Examples.Clear, Base):
    _endpoint = "{model_id}/clear"
    _responses = [403, 404]

    class Query(ModelId, ModelOwner):
        pass


class AddCollaborator(Examples.AddCollaborator, Base, Permissions):
    _endpoint = "{model_id}/collaborators/{email}"
    _method = "PUT"
    _responses = [403, 404]

    class Query(ModelId, ModelOwner, Email):
        pass


class RemoveCollaborator(Examples.RemoveCollaborator, Base):
    _endpoint = "{model_id}/collaborators/{email}"
    _method = "DELETE"
    _responses = [403, 404]

    class Query(ModelId, ModelOwner, Email):
        pass
