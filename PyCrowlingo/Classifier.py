from .Connector import Connector
from .ApiModels import Classifier as Models


class Classifier(Connector):

    def classify(self, model_id, text, lang=None, prod_version=None):
        return Models.Classify.fill(**locals()).call(self.client)

    def create_model(self, model_id, model_type=None):
        return Models.CreateModel.fill(**locals()).call(self.client)

    def deploy_model(self, model_id):
        return Models.DeployModel.fill(**locals()).call(self.client)

    def clear_model(self, model_id):
        return Models.ClearModel.fill(**locals()).call(self.client)

    def train_model(self, model_id, model_type=None):
        return Models.TrainModel.fill(**locals()).call(self.client)

    def create_documents(self, model_id, documents):
        return Models.CreateDocuments.fill(**locals()).call(self.client)

    def update_document(self, model_id, document_id, class_id=None, text=None, lang=None):
        return Models.UpdateDocument.fill(**locals()).call(self.client)

    def list_documents(self, model_id, page=None, page_size=None, sort=None, ascending=None, id=None, lang=None, class_id=None):
        return Models.ListDocuments.fill(**locals()).call(self.client)

    def delete_document(self, model_id, document_id):
        return Models.DeleteDocument.fill(**locals()).call(self.client)

    def delete_model(self, model_id):
        return Models.DeleteModel.fill(**locals()).call(self.client)

    def upload_csv(self, model_id, filename, fieldnames=None, delimiter=",", batch_size=200):
        from .FileUploader import upload_csv

        upload_csv(self.client, Models.CreateDocuments, "documents", **locals())
