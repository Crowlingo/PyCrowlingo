from .Connector import Connector
from .ApiModels import Classifier as Models


class Classifier(Connector):

    def classify(self, model_id, text, lang=None):
        return Models.Classify.fill(**locals()).call(self.client)

    def create_model(self, model_id):
        return Models.CreateModel.fill(**locals()).call(self.client)

    def train_model(self, model_id):
        return Models.TrainModel.fill(**locals()).call(self.client)

    def create_sentence(self, model_id, text, class_id, sentence_id=None, lang=None):
        return Models.CreateSentence.fill(**locals()).call(self.client)

    def delete_sentence(self, model_id, sentence_id):
        return Models.DeleteSentence.fill(**locals()).call(self.client)

    def delete_model(self, model_id):
        return Models.DeleteModel.fill(**locals()).call(self.client)

