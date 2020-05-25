from typing import Optional

from .ApiModels import Multi as Models


class Pipeline:
    def __init__(self, client=None, **commons):
        self._client = client
        self.pipeline = {}
        self.commons = commons

    def add(self, model, **parameters):
        class NewModel(model, model.Query):
            text: Optional[str] = None
            lang: Optional[str] = None

            @staticmethod
            def eid():
                return model.eid()

        new_model = NewModel(**parameters)
        self.pipeline[new_model.eid()] = new_model
        return self

    def call(self):
        return Models.Pipeline.fill(**self.__dict__).call(self._client)


class Bulk:

    def __init__(self, client, pipelines=None, batch_size=20):
        self._client = client
        self._batch_size = batch_size
        self.pipelines = []
        if pipelines:
            for p in pipelines:
                self.add(p)

    def add(self, pipeline):
        self.pipelines.append(Models.Pipeline.fill(**pipeline.__dict__))

    def lazy_call(self):
        for i in range(0, len(self.pipelines), self._batch_size):
            for res in Models.Bulk.fill(pipelines=self.pipelines[i: i + self._batch_size]).call(self._client).responses:
                yield res

    def call(self):
        return list(self.lazy_call())