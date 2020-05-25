from .ApiModels import User as Models
from .Connector import Connector


class User(Connector):

    def login(self, username, password):
        res = Models.Login().call(self.client, username, password)
        self.client.set_token(res.access_token)
        return res

    def usage(self):
        return Models.Usage.fill(**locals()).call(self.client)

    def refresh_token(self, username, password):
        res = Models.RefreshToken().call(self.client, username, password)
        self.client.set_token(res.access_token)
        return res
