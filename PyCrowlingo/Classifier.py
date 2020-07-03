from .Connector import Connector
from .ApiModels import Classifier as Models


class Classifier(Connector):

    def classify(self, model_id, text, model_owner=None, lang=None, prod_version=None, optional_features=None):
        return Models.Classify.fill(**locals()).call(self.client)

    def create_documents(self, model_id, documents, model_owner=None):
        return Models.CreateDocuments.fill(**locals()).call(self.client)

    def update_document(self, model_id, document_id, model_owner=None, class_id=None, text=None, lang=None):
        return Models.UpdateDocument.fill(**locals()).call(self.client)

    def get_document(self, model_id, document_id, model_owner=None):
        return Models.GetDocument.fill(**locals()).call(self.client)

    def list_documents(self, model_id, model_owner=None, page=None, page_size=None, sort=None, ascending=None, id=None, lang=None, class_id=None):
        return Models.ListDocuments.fill(**locals()).call(self.client)

    def delete_document(self, model_id, document_id, model_owner=None):
        return Models.DeleteDocument.fill(**locals()).call(self.client)

    def upload_csv(self, model_id, filename, model_owner=None, fieldnames=None, delimiter=",", batch_size=200):
        from .FileUploader import upload_csv

        upload_csv(self.client, Models.CreateDocuments, "documents", **locals())
