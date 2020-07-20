from .Connector import Connector

from .ApiModels import Concepts as Models


class Concepts(Connector):

    def extract(self, text, lang=None, properties=None, precision=None, split=None):
        return Models.Extract.fill(**locals()).call(self.client)

    def extract_custom(self, model_id, text, lang=None, properties=None, model_owner=None, prod_version=None):
        return Models.ExtractCustom.fill(**locals()).call(self.client)

    def create_concepts(self, model_id, concepts, model_owner=None):
        return Models.CreateConcepts.fill(**locals()).call(self.client)

    def create_labels(self, model_id, labels, model_owner=None):
        return Models.CreateLabels.fill(**locals()).call(self.client)

    def update_concept(self, model_id, concept_id, model_owner=None,  properties=None):
        return Models.UpdateConcept.fill(**locals()).call(self.client)

    def update_label(self, model_id, label_id, model_owner=None, text=None, lang=None, concept_id=None):
        return Models.UpdateLabel.fill(**locals()).call(self.client)

    def delete_label(self, model_id, label_id, model_owner=None):
        return Models.DeleteLabel.fill(**locals()).call(self.client)

    def delete_concept(self, model_id, concept_id, model_owner=None):
        return Models.DeleteConcept.fill(**locals()).call(self.client)

    def get_concept(self, model_id, concept_id, model_owner=None):
        return Models.GetConcept.fill(**locals()).call(self.client)

    def get_label(self, model_id, label_id, model_owner=None):
        return Models.GetLabel.fill(**locals()).call(self.client)

    def list_concepts(self, model_id, model_owner=None, page=None, page_size=None, sort=None, id=None):
        return Models.ListConcepts.fill(**locals()).call(self.client)

    def list_labels(self, model_id, model_owner=None, page=None, page_size=None, sort=None, ascending=None,
                    id=None, text=None, lang=None, concept_id=None):
        return Models.ListLabels.fill(**locals()).call(self.client)

    def upload_csv_concepts(self, model_id, filename, model_owner=None, fieldnames=None, delimiter=",", batch_size=200):
        from .FileUploader import upload_csv

        upload_csv(self.client, Models.CreateConcepts, "concepts", **locals())

    def upload_csv_labels(self, model_id, filename, model_owner=None, fieldnames=None, delimiter=",", batch_size=200):
        from .FileUploader import upload_csv

        upload_csv(self.client, Models.CreateLabels, "labels", **locals())
