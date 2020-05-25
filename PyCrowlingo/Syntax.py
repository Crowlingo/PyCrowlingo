from .Connector import Connector

from .ApiModels import Syntax as Models


class Syntax(Connector):

    def extract(self, text, lang=None, visualize=None):
        return Models.Extract.fill(**locals()).call(self.client)
