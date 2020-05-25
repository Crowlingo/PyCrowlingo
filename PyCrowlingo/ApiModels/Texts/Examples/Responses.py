from pydantic import BaseModel


class Similarity(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                'similarity': 0.8926192789106295
            }
        }
