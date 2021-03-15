from PyCrowlingo.Errors import TrainingError

from .Connector import Connector
from .ApiModels import Model as Models


class Model(Connector):

    def get(self, model_id):
        return Models.Get.fill(**locals()).call(self.client)

    def create(self, name, category, metadata=None):
        return Models.Create.fill(**locals()).call(self.client)

    def deploy(self, model_id):
        return Models.Deploy.fill(**locals()).call(self.client)

    def clear(self, model_id):
        return Models.Clear.fill(**locals()).call(self.client)

    def train(self, model_id, model_type=None, train_ratio=None, max_training_time=None,
              hyper_parameters=None, nb_trainings=None):
        return Models.Train.fill(**locals()).call(self.client)

    def delete(self, model_id):
        return Models.Delete.fill(**locals()).call(self.client)

    def add_collaborator(self, model_id, email, permissions=None):
        return Models.AddCollaborator.fill(**locals()).call(self.client)

    def remove_collaborator(self, model_id, email):
        return Models.RemoveCollaborator.fill(**locals()).call(self.client)

    def edit(self, model_id, description=None, markers=None, public=None, readme=None):
        return Models.Edit.fill(**locals()).call(self.client)

    def list_public(self, page=None, page_size=None, markers=None):
        return Models.ListPublic.fill(**locals()).call(self.client)

    def list_user(self, page=None, page_size=None, markers=None):
        return Models.ListUser.fill(**locals()).call(self.client)

    def wait_training(self, model_id, time_sleep=3):
        import time
        from dateutil.parser import parse
        from tqdm import tqdm

        done = False
        res = None
        with tqdm(total=100) as pbar:
            while not done:
                time.sleep(time_sleep)
                res = self.client.model.get(model_id)
                status = res.training_status
                pbar.n = res.training_progress
                pbar.refresh()
                done = status == 'done'
                if status == "error":
                    raise TrainingError(res.training_error)
        start = parse(res.training_start)
        end = parse(res.training_end)
        print(f"Trained {model_id} in {end - start}")
        return res.versions["test"].metrics

    def wait_deploying(self, model_id, time_sleep=3):
        import time
        from dateutil.parser import parse
        from tqdm import tqdm

        done = False
        res = None
        with tqdm(total=100) as pbar:
            while not done:
                time.sleep(time_sleep)
                res = self.client.model.get(model_id)
                status = res.training_status
                pbar.n = res.training_progress
                pbar.refresh()
                done = status == 'done'
                if status == "error":
                    raise TrainingError(res.training_error)
        start = parse(res.deploying_start)
        end = parse(res.deploying_end)
        print(f"Deployed {model_id} in {end - start}")
        return res