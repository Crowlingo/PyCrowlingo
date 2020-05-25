from .Connector import Connector

from .ApiModels import Entities as Models


class Entities(Connector):

    def extract(self, text, lang=None, visualize=None):
        return Models.Extract.fill(**locals()).call(self.client)

    def duckling(self, text, lang=None):
        return Models.Duckling.fill(**locals()).call(self.client)
