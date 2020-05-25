import logging
from typing import Any, Dict, Optional, Text

from rasa.nlu.classifiers import classifier
from rasa.nlu.config import RasaNLUModelConfig
from rasa.nlu.training_data import Message, TrainingData
from requests import HTTPError

from .. import Client
from ..ApiModels import Classifier
from ..Multi import Bulk, Pipeline

logger = logging.getLogger(__name__)


class IntentClassifier(classifier.IntentClassifier):
    """Classify intent in 100+ languages no matter the training language"""

    def __init__(self, component_config: Optional[Dict[Text, Any]] = None) -> None:
        super().__init__(component_config)
        self.client = Client(component_config["token"])
        self.model_id = component_config["model_id"]

    def process(self, message: Message, **kwargs: Any) -> None:
        """Return the most likely intent and its probability for a message."""

        res = self.client.classifier.classify(self.model_id, message.text)
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
            self.client.classifier.delete_model(self.model_id)
        except HTTPError:
            pass
        self.client.classifier.create_model(self.model_id)
        bulk = Bulk(self.client)
        for message in training_data.training_examples:
            bulk.add(Pipeline().add(Classifier.CreateSentence, model_id=self.model_id, text=message.text,
                                    class_id=message.get("intent")))
        bulk.call()
        self.client.classifier.train_model(self.model_id)
