import os

from PyCrowlingo import Client


def get_client(config):
    config = config or {}
    token = os.environ.get("CROWLINGO_TOKEN", config.get("token"))
    username = os.environ.get("CROWLINGO_USERNAME", config.get("username"))
    password = os.environ.get("CROLWINGO_PASSWORD", config.get("password"))
    url = os.environ.get("CROWLINGO_URL", config.get("url", "https://crowlingo.com/api/v1"))
    return Client(token, username=username, password=password, url=url)
