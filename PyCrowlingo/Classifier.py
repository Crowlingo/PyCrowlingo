from .Connector import Connector
from .ApiModels import Classifier as Models


class Classifier(Connector):

    def classify(self, model_id, text, lang=None, prod_version=None, optional_features=None):
        return Models.Classify.fill(**locals()).call(self.client)

    def create_documents(self, model_id, documents, upsert=None):
        return Models.CreateDocuments.fill(**locals()).call(self.client)

    def update_document(self, model_id, document_id, class_id=None, text=None, lang=None, markers=None):
        return Models.UpdateDocument.fill(**locals()).call(self.client)

    def get_document(self, model_id, document_id):
        return Models.GetDocument.fill(**locals()).call(self.client)

    def list_documents(self, model_id, page=None, page_size=None, id=None, lang=None, class_id=None, marker=None):
        return Models.ListDocuments.fill(**locals()).call(self.client)

    def delete_document(self, model_id, document_id):
        return Models.DeleteDocument.fill(**locals()).call(self.client)

    def rename_class(self, model_id, old_class_id, new_class_id):
        return Models.RenameClass.fill(**locals()).call(self.client)

    def upload_csv(self, model_id, filename, fieldnames=None, delimiter=",", batch_size=200):
        from .FileUploader import upload_csv

        upload_csv(self.client, Models.CreateDocuments, "documents", **locals())
