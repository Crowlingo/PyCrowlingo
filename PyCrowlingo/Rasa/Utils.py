from PyCrowlingo import Client


def get_client(config):
    config = config or {}
    return Client(config.get("token"),
                  username=config.get("username"),
                  password=config.get("password"))
