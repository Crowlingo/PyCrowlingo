from PyCrowlingo.Errors import TrainingError

from .Connector import Connector
from .ApiModels import Model as Models


class Model(Connector):

    def get(self, model_id, model_owner=None):
        return Models.Get.fill(**locals()).call(self.client)

    def create(self, model_id, category, model_type=None, metadata=None):
        return Models.Create.fill(**locals()).call(self.client)

    def deploy(self, model_id, model_owner=None):
        return Models.Deploy.fill(**locals()).call(self.client)

    def clear(self, model_id, model_owner=None):
        return Models.Clear.fill(**locals()).call(self.client)

    def train(self, model_id, model_owner=None, model_type=None, model_config=None):
        return Models.Train.fill(**locals()).call(self.client)

    def delete(self, model_id, model_owner=None):
        return Models.Delete.fill(**locals()).call(self.client)

    def add_collaborator(self, model_id, email, permissions=None, model_owner=None):
        return Models.AddCollaborator.fill(**locals()).call(self.client)

    def remove_collaborator(self, model_id, email, model_owner=None):
        return Models.RemoveCollaborator.fill(**locals()).call(self.client)

    def wait_training(self, model_id, model_owner=None, time_sleep=3):
        import time

        done = False
        res = None
        while not done:
            time.sleep(time_sleep)
            res = self.client.model.get(model_id, model_owner)
            status = res.training_status
            done = status == 'done'
            if status == "error":
                raise TrainingError(res.training_error)
        return res.metrics
