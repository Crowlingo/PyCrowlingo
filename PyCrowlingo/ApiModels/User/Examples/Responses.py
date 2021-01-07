from pydantic import BaseModel


class Usage(BaseModel):
    class Config:
        schema_extra = {
            "example":
                {
                    "cur_minute": 0,
                    "cur_period": 75,
                    "minute_limit": 60,
                    "period_limit": 300,
                    "models_limit": 1,
                    "minute_reset": '2020-06-06 12:08:07.973342',
                    "period_reset": '2020-06-30 12:48:07.973339'
                }
        }


class Login(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                "access_token": "eyJ0eXAiOiJKV1QiLC",
                "user_type": "default",
            }
        }


class RefreshToken(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                "access_token": "eyJ0eXAiOiJKV1QiLC",
            }
        }


class Info(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                "email": "john@crowlingo.com",
                "plan": "free"
            }
        }
