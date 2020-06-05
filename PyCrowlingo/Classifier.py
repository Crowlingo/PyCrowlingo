from .Connector import Connector
from .ApiModels import Classifier as Models


class Classifier(Connector):

    def classify(self, model_id, text, lang=None, prod_version=None):
        return Models.Classify.fill(**locals()).call(self.client)

    def create_model(self, model_id):
        return Models.CreateModel.fill(**locals()).call(self.client)

    def deploy_model(self, model_id):
        return Models.DeployModel.fill(**locals()).call(self.client)

    def clear_model(self, model_id):
        return Models.ClearModel.fill(**locals()).call(self.client)

    def train_model(self, model_id):
        return Models.TrainModel.fill(**locals()).call(self.client)

    def create_sentence(self, model_id, text, class_id, sentence_id=None, lang=None):
        return Models.CreateSentence.fill(**locals()).call(self.client)

    def delete_sentence(self, model_id, sentence_id, model_version=None):
        return Models.DeleteSentence.fill(**locals()).call(self.client)

    def delete_model(self, model_id):
        return Models.DeleteModel.fill(**locals()).call(self.client)

