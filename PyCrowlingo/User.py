from .ApiModels import User as Models
from .Connector import Connector


class User(Connector):

    def login(self, username, password):
        res = Models.Login.fill().call(self.client, username, password)
        self.client.set_token(res.access_token)
        self.client._plan = res.plan
        return res

    def usage(self):
        return Models.Usage.fill(**locals()).call(self.client)

    def info(self):
        res = Models.Info.fill(**locals()).call(self.client)
        self.client._plan = res.plan
        return res

    def refresh_token(self, username, password):
        res = Models.RefreshToken.fill().call(self.client, username, password)
        self.client.set_token(res.access_token)
        return res
