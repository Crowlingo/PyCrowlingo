from .Connector import Connector

from .ApiModels import Faq as Models


class Faq(Connector):

    def search(self, model_id, text, lang=None, variations=None):
        return Models.Search.fill(**locals()).call(self.client)

    def train_model(self, model_id):
        return Models.TrainModel.fill(**locals()).call(self.client)

    def create_model(self, model_id):
        return Models.CreateModel.fill(**locals()).call(self.client)

    def create_question(self, model_id, variations, id=None, answer_id=None):
        return Models.CreateQuestion.fill(**locals()).call(self.client)

    def create_answer(self, model_id, variations, id=None):
        return Models.CreateAnswer.fill(**locals()).call(self.client)

    def delete_model(self, model_id):
        return Models.DeleteModel.fill(**locals()).call(self.client)

    def delete_question(self, model_id, question_id):
        return Models.DeleteQuestion.fill(**locals()).call(self.client)

    def delete_answer(self, model_id, answer_id):
        return Models.DeleteAnswer.fill(**locals()).call(self.client)
