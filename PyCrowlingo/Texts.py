from .Connector import Connector

from .ApiModels import Texts as Models


class Texts(Connector):

    def similarity(self, text, text2, lang=None, lang2=None):
        return Models.Similarity.fill(**locals()).call(self.client)
