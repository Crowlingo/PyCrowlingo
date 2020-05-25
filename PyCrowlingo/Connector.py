class Connector:

    def __init__(self, client):
        self.client = client

    def call(self, endpoint, params):
        return self.client.call(endpoint, params)
