from pydantic import BaseModel


class Extract(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                'summary': ["Some of Australia's largest cities have also been affected, including Melbourne and "
                            "Sydney -- where fires have damaged homes in the outer suburbs and thick plumes of smoke "
                            "have blanketed the urban center."]
            }
        }

