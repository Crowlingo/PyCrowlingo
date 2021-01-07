from pydantic import BaseModel


class Login(BaseModel):
    class Config:
        schema_extra = {
            "_python": [f"username = \"[USERNAME]\"", f"password = \"[PASSWORD]\"",
                        "client.user.login(username, password)"]
        }


class Usage(BaseModel):
    class Config:
        schema_extra = {
            "_python": ["client.user.usage()"]
        }


class RefreshToken(BaseModel):
    class Config:
        schema_extra = {
            "_python": [f"username = \"[USERNAME]\"", f"password = \"[PASSWORD]\"",
                        "client.user.refresh_token(username, password)"]
        }


class Info(BaseModel):
    class Config:
        schema_extra = {
            "_python": ["client.user.info()"]
        }
