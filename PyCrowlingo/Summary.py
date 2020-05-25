from .Connector import Connector

from .ApiModels import Summary as Models


class Summary(Connector):

    def extract(self, text, lang=None, ratio=None, nb_sentences=None):
        return Models.Extract.fill(**locals()).call(self.client)
