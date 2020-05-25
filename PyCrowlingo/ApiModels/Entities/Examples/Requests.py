from pydantic import BaseModel


class Extract(BaseModel):
    class Config:
        _text = "On 26 April 1986, Chernobyl suffered the world’s worst nuclear disaster. An experiment designed to " \
                "test the safety of the power plant went wrong and caused a fire which spewed radiation for 10 days. " \
                "Clouds carrying radioactive particles drifted for thousands of miles, releasing toxic rain all over " \
                "Europe. Those living close to Chernobyl - about 116,000 people - were immediately evacuated. A 30 km " \
                "exclusion zone was imposed around the damaged reactor. This was later expanded to cover more " \
                "affected areas. "
        schema_extra = {
            "example": {"text": _text},
            "_python": [f"text = \"{_text}\"",
                        "client.entities.extract(text)"]
        }


class Duckling(BaseModel):
    class Config:
        _text = "On 26 April 1986, Chernobyl suffered the world’s worst nuclear disaster. An experiment designed to " \
                "test the safety of the power plant went wrong and caused a fire which spewed radiation for 10 days. " \
                "Clouds carrying radioactive particles drifted for thousands of miles, releasing toxic rain all over " \
                "Europe. Those living close to Chernobyl - about 116,000 people - were immediately evacuated. A 30 km " \
                "exclusion zone was imposed around the damaged reactor. This was later expanded to cover more " \
                "affected areas. "
        schema_extra = {
            "example": {"text": _text},
            "_python": [f"text = \"{_text}\"",
                        "client.entities.duckling(text)"]
        }
