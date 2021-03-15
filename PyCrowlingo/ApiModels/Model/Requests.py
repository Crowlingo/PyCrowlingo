from typing import Union, Optional, Dict, Any

from pydantic import BaseModel, Field, PositiveInt

from . import Responses
from .Examples import Requests as Examples
from ..Attributes import ModelId, ModelConfig, Permissions, Email, Category, Name, Description, Markers, \
    Public, Pagination, ModelType, TrainRatio, MaxTrainingTime, HyperParameters, NbTrainings, Readme
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

    class Query(ModelId):
        pass


class Train(Examples.Train, Base, ModelType, TrainRatio, MaxTrainingTime, HyperParameters, NbTrainings):
    _endpoint = "{model_id}/train"
    _price = 1
    _responses = [403, 404]

    class Query(ModelId):
        pass


class Create(Examples.Create, Base):
    _endpoint = "{category}/{name}"
    _responses = [403, 409]

    class Query(BasicModel, Name):
        category: Category


class Delete(Examples.Delete, Base):
    _endpoint = "{model_id}"
    _method = "DELETE"
    _responses = [403, 404]

    class Query(ModelId):
        pass


class Deploy(Examples.Deploy, Base):
    _endpoint = "{model_id}/deploy"
    _responses = [403, 404]

    class Query(ModelId):
        pass


class Clear(Examples.Clear, Base):
    _endpoint = "{model_id}/clear"
    _responses = [403, 404]

    class Query(ModelId):
        pass


class AddCollaborator(Examples.AddCollaborator, Base, Permissions):
    _endpoint = "{model_id}/collaborators/{email}"
    _method = "PUT"
    _responses = [403, 404]

    class Query(ModelId, Email):
        pass


class RemoveCollaborator(Examples.RemoveCollaborator, Base):
    _endpoint = "{model_id}/collaborators/{email}"
    _method = "DELETE"
    _responses = [403, 404]

    class Query(ModelId, Email):
        pass


class Edit(Examples.Edit, Base, Description, Markers, Public, Readme):
    _endpoint = "{model_id}"
    _method = "PATCH"
    _responses = [403, 404]

    class Query(ModelId):
        pass


class ListPublic(Examples.ListPublic, Base, Pagination, Markers):
    _endpoint = "list/public"
    _method = "GET"
    _responses = []

    class Query(BaseModel):
        pass


class ListUser(Examples.ListUser, Base, Pagination, Markers):
    _endpoint = "list/user"
    _method = "GET"
    _responses = []

    class Query(BaseModel):
        pass
