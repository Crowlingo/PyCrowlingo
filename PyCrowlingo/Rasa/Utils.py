from PyCrowlingo import Client


def get_client(config):
    config = config or {}
    print(config)
    return Client(config.get("token"),
                  username=config.get("username"),
                  password=config.get("password"),
                  url=config.get("url", "https://crowlingo.com/api/v1"))
