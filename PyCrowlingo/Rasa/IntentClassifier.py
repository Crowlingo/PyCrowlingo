import logging
from typing import Any, Dict, Optional, Text

from rasa.nlu.classifiers import classifier
from rasa.nlu.config import RasaNLUModelConfig
from rasa.nlu.training_data import Message, TrainingData

from .Utils import get_client
from ..Errors import ModelNotFound

logger = logging.getLogger(__name__)


class IntentClassifier(classifier.IntentClassifier):
    """Classify intent in 100+ languages no matter the training language"""

    def __init__(self, component_config: Optional[Dict[Text, Any]] = None) -> None:
        super().__init__(component_config)
        self.client = get_client(component_config)
        self.model_id = component_config.get("model_id")
        self.model_owner = component_config.get("model_owner")
        self.prod_version = component_config.get("prod_version")

    def process(self, message: Message, **kwargs: Any) -> None:
        """Return the most likely intent and its probability for a message."""

        res = self.client.classifier.classify(self.model_id, message.text, model_owner=self.model_owner,
                                              prod_version=self.prod_version)
        intent_ranking = [
            {"name": intent.class_id, "confidence": intent.confidence}
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
            self.client.model.clear(self.model_id, model_owner=self.model_owner)
        except ModelNotFound:
            self.client.model.create(self.model_id, "clf")
            self.model_owner = None
            self.prod_version = None
        docs = []
        for message in training_data.training_examples:
            docs.append({"text": message.text, "class_id": message.get("intent")})
        self.client.classifier.create_documents(self.model_id, docs, model_owner=self.model_owner)
        self.client.model.train(self.model_id, model_owner=self.model_owner)
