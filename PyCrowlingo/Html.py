from .Connector import Connector

from .ApiModels import Html as Models


class Html(Connector):

    def extract_article(self, url, properties=None, concepts_properties=None,
                        precision=None, normalizations=None, split=None, model_id=None):
        return Models.ExtractArticle.fill(**locals()).call(self.client)
