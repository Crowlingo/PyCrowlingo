from pydantic import BaseModel


class Usage(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                'cur_rate': 0,
                'rate_limit': 30,
                'month_requests': 93,
                'monthly_limit': 300
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
