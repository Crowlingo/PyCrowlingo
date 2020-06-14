from .Connector import Connector

from .ApiModels import News as Models


class News(Connector):

    def domain_urls(self, domain, cursor=None):
        return Models.DomainUrls.fill(**locals()).call(self.client)
