import logging
from typing import Any, Dict, Optional, Text

from rasa.nlu.classifiers import classifier
from rasa.nlu.config import RasaNLUModelConfig
from rasa.shared.nlu.constants import TEXT, INTENT
from rasa.nlu.model import Metadata
from rasa.shared.nlu.training_data.message import Message
from rasa.shared.nlu.training_data.training_data import TrainingData
import rasa.utils.io as io_utils
from uuid import uuid4
import os
from PyCrowlingo.ApiModels.Attributes import ID_TYPE
from pydantic.errors import StrRegexError

from .Utils import get_client
from ..Errors import ModelNotFound

logger = logging.getLogger(__name__)


class IntentClassifier(classifier.IntentClassifier):
    """Classify intent in 100+ languages no matter the training language"""

    def __init__(self, component_config: Optional[Dict[Text, Any]] = None,
                 class_encoder: Optional[Dict[str, str]] = None) -> None:
        super().__init__(component_config)
        self.client = get_client(component_config)
        self.model_id = component_config.get("model_id")
        self.prod_version = component_config.get("prod_version")
        self.model_type = component_config.get("model_type")
        self.train_ratio = component_config.get("train_ratio", 1.0)
        self.max_training_time = component_config.get("max_training_time")
        self.hyper_parameters = component_config.get("hyper_parameters")
        self.nb_trainings = component_config.get("nb_trainings")
        self.class_encoder = class_encoder or {}

    def process(self, message: Message, **kwargs: Any) -> None:
        """Return the most likely intent and its probability for a message."""

        res = self.client.classifier.classify(self.model_id, message.get(TEXT),
                                              prod_version=self.prod_version)
        intent_ranking = [
            {"name": self.class_encoder.get(intent.class_id, intent.class_id), "confidence": intent.confidence}
            for intent in res.classes
        ]
        intent = intent_ranking[0]
        message.set("intent", intent, add_to_output=True)
        message.set("intent_ranking", intent_ranking, add_to_output=True)

    def train(self, training_data: TrainingData, config: Optional[RasaNLUModelConfig] = None, **kwargs: Any) -> None:
        """Train this component.

        This is the components chance to train itself provided
        with the training data. The component can rely on
        any context attribute to be present, that gets created
        by a call to :meth:`rasa.nlu.components.Component.create`
        of ANY component and
        on any context attributes created by a call to
        :meth:`rasa.nlu.components.Component.train`
        of components previous to this one.

        Args:
            training_data:
                The :class:`rasa.nlu.training_data.training_data.TrainingData`.
            config: The model configuration parameters.

        """
        try:
            self.client.model.clear(self.model_id)
        except ModelNotFound:
            self.client.model.create(self.model_id, "classifier")
            self.prod_version = None
        docs = []
        intent_to_class = {}
        for message in training_data.training_examples:
            if message.get(TEXT):
                intent = message.get(INTENT)
                try:
                    ID_TYPE.validate(intent)
                    class_id = intent
                except StrRegexError:
                    class_id = intent_to_class.get(intent)
                    if not class_id:
                        class_id = str(uuid4())
                        intent_to_class[intent] = class_id
                docs.append({"text": message.get(TEXT), "class_id": class_id})
        self.client.classifier.create_documents(self.model_id, docs)
        self.client.model.train(self.model_id, model_type=self.model_type, train_ratio=self.train_ratio,
                                max_training_time=self.max_training_time, hyper_parameters=self.hyper_parameters,
                                nb_trainings=self.nb_trainings)
        self.client.model.wait_training(self.model_id)
        self.class_encoder = {v: k for k, v in intent_to_class.items()}

    def persist(self, file_name: Text, model_dir: Text) -> Optional[Dict[Text, Any]]:
        """Persist this model into the passed directory."""

        class_encoder_file_name = file_name + "class_encoder.pkl"
        if self.class_encoder:
            io_utils.json_pickle(os.path.join(model_dir, class_encoder_file_name), self.class_encoder)
        return {"class_encoder": class_encoder_file_name}

    @classmethod
    def load(cls, meta: Dict[Text, Any], model_dir: Optional[Text] = None, model_metadata: Optional[Metadata] = None,
        cached_component: Optional["SklearnIntentClassifier"] = None, **kwargs: Any) -> "SklearnIntentClassifier":
        class_encoder_file = os.path.join(model_dir, meta.get("class_encoder"))
        if os.path.exists(class_encoder_file):
            class_encoder = io_utils.json_unpickle(class_encoder_file)
            return cls(meta, class_encoder)
        else:
            return cls(meta)