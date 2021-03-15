import re
from enum import Enum
from typing import Optional

from pydantic import BaseModel
from requests import HTTPError

from .ApiModels.Attributes import Error


class CrowlingoExceptionModel(BaseModel):
    detail: Optional[Error]


class CrowlingoException(HTTPError):

    def __init__(self, status_code, msg, headers=None):
        self.status_code = status_code
        self.detail = {"msg": msg, "error_id": re.sub(r'(?<!^)(?=[A-Z])', '_', self.__class__.__name__).upper()}
        self.headers = {}
        self.set_headers(headers)

    def __str__(self):
        return f"[{self.status_code}] - {self.detail['error_id']}: {self.detail['msg']}"

    def set_headers(self, headers):
        if headers:
            self.headers = dict(headers)


class InternalError(CrowlingoException):

    def __init__(self, headers=None):
        super().__init__(500, "Internal Error, please contact an administrator if it happens again", headers)


class ModelNotTrained(CrowlingoException):

    def __init__(self, headers=None):
        super().__init__(423, "This model is not trained yet. You have to wait until it is trained or "
                              "run the training before performing this action.", headers)


class BadCredentials(CrowlingoException):

    def __init__(self, headers=None):
        super().__init__(401, "Could not validate credentials. There might be an error in your token or "
                              "email/password. Maybe your account has been disabled. "
                              "If the problem persists, please contact us.", headers)


class TestModelForbidden(CrowlingoException):

    def __init__(self, headers=None):
        super().__init__(403, "You do not have access to the test version of this model. Ask the access to the owner of"
                              " the model or use the production version of this model", headers)


class BadModelPerms(CrowlingoException):

    def __init__(self, headers=None):
        super().__init__(403, "You do not have the permissions to perform this action on this model. "
                              "Ask the owner of this model to get permission.", headers)


class BadModelCategory(CrowlingoException):

    def __init__(self, headers=None):
        super().__init__(404, "This model cannot be use for this kind of request. "
                              "Create a new model or use another endpoint.", headers)


class ModelNotDeployed(CrowlingoException):

    def __init__(self, headers=None):
        super().__init__(404, "This model is not deployed. Use the test model or deploy it first.", headers)


class TokenNotFound(CrowlingoException):

    def __init__(self, headers=None):
        super().__init__(401, "Token not found. Insert your token in the query parameter by "
                              "api_key=[YOUR_TOKEN]  or in the headers by x-api-key:[YOUR TOKEN].", headers)


class CollaboratorNotFound(CrowlingoException):

    def __init__(self, headers=None):
        super().__init__(404, "This collaborator was not found.", headers)


class ModelNotFound(CrowlingoException):

    def __init__(self, headers=None):
        super().__init__(404, "Model not Found. You have to create a model before using it.", headers)


class DocumentNotFound(CrowlingoException):

    def __init__(self, headers=None):
        super().__init__(404, "Document not Found. You have to create a document before using it.", headers)


class MinuteLimitReached(CrowlingoException):

    def __init__(self, headers=None):
        super().__init__(429, "Minute limit reached, wait the number of seconds indicated by "
                              "the header: x-minute-reset or upgrade your subscription plan.", headers)


class PeriodLimitReached(CrowlingoException):

    def __init__(self, headers=None):
        super().__init__(429, "Period limit reached, wait the number of seconds indicated by "
                              "the header: x-period-reset or upgrade your subscription plan.", headers)


class ModelsLimitReached(CrowlingoException):

    def __init__(self, headers=None):
        super().__init__(429, "You have reached the maximal number of custom models allowed. "
                              "If you want to create a new one, you have to delete one of your custom models first "
                              "or upgrade your subscription plan.", headers)


class DuplicateModelId(CrowlingoException):

    def __init__(self, headers=None):
        super().__init__(409, "You already have a model with this id, please delete the model first if you want "
                              "to overwrite it",
                         headers)


class DuplicateDocumentId(CrowlingoException):

    def __init__(self, headers=None):
        super().__init__(409, "You already have a document with this id, please delete the document first if you want "
                              "to overwrite it or use the parameter 'upsert' to overwrite it.",
                         headers)


class BadParametersQuery(CrowlingoException):

    def __init__(self, headers=None):
        super().__init__(422, "Query's parameters do not match with documentation description. "
                              "The query cannot be processed.", headers)


class ContentLengthRequired(CrowlingoException):
    def __init__(self, headers=None):
        super().__init__(411, "You need to provide a content length parameter in headers for POST and PATCH requests.",
                         headers)


class RequestEntityTooLarge(CrowlingoException):

    def __init__(self, headers=None):
        super().__init__(413, "The payload of your body is too large. Try to split your request with smaller payload.",
                         headers)


class TrainingError(CrowlingoException):

    def __init__(self, msg, headers=None):
        prefix = "An error happened during the training: "
        msg = str(msg)
        msg = f"{prefix}{msg}" if not msg.startswith(prefix) else msg
        super().__init__(400, msg, headers)


class BadEnvironmentPerms(CrowlingoException):

    def __init__(self, headers=None):
        super().__init__(403, "You do not have the permission to query this URL."
                              "Use the endpoint linked to your environment. "
                              "If the problem persists, please contact us.", headers)


class NoTrainingData(CrowlingoException):

    def __init__(self, headers=None):
        super().__init__(400, "There is no training data associated to this model. Add some documents before running "
                         "the train process", headers)


class MinTrainingClasses(CrowlingoException):

    def __init__(self, headers=None):
        super().__init__(400, "You must have at least 2 different classes in your data to train a classifier.", headers)


# ####### FULL #######


class BadAdminPerms(CrowlingoException):

    def __init__(self, headers=None):
        super().__init__(403, "You do not have the permission to do this action."
                              "If the problem persists, please contact us.", headers)


class SubscriptionNotFound(CrowlingoException):

    def __init__(self, headers=None):
        super().__init__(404, "No subscription was found for this kind of plan. "
                              "Modify user's custom parameters for a custom plan.", headers)


class DuplicateEmail(CrowlingoException):

    def __init__(self, headers=None):
        super().__init__(409, "This email is already in use.", headers)


class AlreadySubscribed(CrowlingoException):

    def __init__(self, headers=None):
        super().__init__(404, "The user has already subscribed to this plan.", headers)


class ErrorsEnum(Enum):
    INTERNAL_ERROR = InternalError
    MODEL_NOT_TRAINED = ModelNotTrained
    BAD_CREDENTIALS = BadCredentials
    TEST_MODEL_FORBIDDEN = TestModelForbidden
    BAD_MODEL_PERMS = BadModelPerms
    BAD_MODEL_CATEGORY = BadModelCategory
    MODEL_NOT_DEPLOYED = ModelNotDeployed
    TOKEN_NOT_FOUND = TokenNotFound
    COLLABORATOR_NOT_FOUND = CollaboratorNotFound
    MODEL_NOT_FOUND = ModelNotFound
    DOCUMENT_NOT_FOUND = DocumentNotFound
    MINUTE_LIMIT_REACHED = MinuteLimitReached
    PERIOD_LIMIT_REACHED = PeriodLimitReached
    MODELS_LIMIT_REACHED = ModelsLimitReached
    DUPLICATE_MODEL_ID = DuplicateModelId
    DUPLICATE_DOCUMENT_ID = DuplicateDocumentId
    BAD_PARAMETERS_QUERY = BadParametersQuery
    CONTENT_LENGTH_REQUIRED = ContentLengthRequired
    REQUEST_ENTITY_TOO_LARGE = RequestEntityTooLarge
    TRAINING_ERROR = TrainingError

    # ###### FULL ########
    BAD_ADMIN_PERMS = BadAdminPerms
    SUBSCRIPTION_NOT_FOUND = SubscriptionNotFound
    DUPLICATE_EMAIL = DuplicateEmail
    ALREADY_SUBSCRIBED = AlreadySubscribed
    NO_TRAINING_DATA = NoTrainingData
