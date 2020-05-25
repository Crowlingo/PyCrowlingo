from pydantic import BaseModel


class Extract(BaseModel):
    class Config:
        _text = "There were things in the shadows; a metal pail, a mop, rags."
        schema_extra = {
            "example": {
                "text": _text
            },

            "_python": [f"text = \"{_text}\"",
                        "client.syntax.extract(text)"]
        }
