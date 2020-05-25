from .Connector import Connector

from .ApiModels import Languages as Models


class Languages(Connector):

    def detect(self, text):
        return Models.Detect.fill(**locals()).call(self.client)
