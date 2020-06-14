from .Connector import Connector

from .ApiModels import Concepts as Models


class Concepts(Connector):

    def extract(self, text, lang=None, properties=None, precision=None, split=None, model_id=None):
        return Models.Extract.fill(**locals()).call(self.client)

    def train_model(self, model_id):
        return Models.TrainModel.fill(**locals()).call(self.client)

    def create_model(self, model_id):
        return Models.CreateModel.fill(**locals()).call(self.client)

    def deploy_model(self, model_id):
        return Models.DeployModel.fill(**locals()).call(self.client)

    def clear_model(self, model_id):
        return Models.ClearModel.fill(**locals()).call(self.client)

    def create_concepts(self, model_id, concepts):
        return Models.CreateConcepts.fill(**locals()).call(self.client)

    def create_labels(self, model_id, labels):
        return Models.CreateLabels.fill(**locals()).call(self.client)

    def update_concept(self, model_id, concept_id, properties=None):
        return Models.UpdateConcept.fill(**locals()).call(self.client)

    def update_label(self, model_id, label_id, text=None, lang=None, concept_id=None):
        return Models.UpdateLabel.fill(**locals()).call(self.client)

    def delete_model(self, model_id):
        return Models.DeleteModel.fill(**locals()).call(self.client)

    def delete_label(self, model_id, label_id):
        return Models.DeleteLabel.fill(**locals()).call(self.client)

    def delete_concept(self, model_id, concept_id):
        return Models.DeleteConcept.fill(**locals()).call(self.client)

    def list_concepts(self, model_id, page=None, page_size=None, sort=None, id=None):
        return Models.ListConcepts.fill(**locals()).call(self.client)

    def list_labels(self, model_id, page=None, page_size=None, sort=None, ascending=None, id=None, text=None, lang=None, concept_id=None):
        return Models.ListLabels.fill(**locals()).call(self.client)

    def upload_csv_concepts(self, model_id, filename, fieldnames=None, delimiter=",", batch_size=200):
        from .FileUploader import upload_csv

        upload_csv(self.client, Models.CreateConcepts, "concepts", **locals())

    def upload_csv_labels(self, model_id, filename, fieldnames=None, delimiter=",", batch_size=200):
        from .FileUploader import upload_csv

        upload_csv(self.client, Models.CreateLabels, "labels", **locals())
