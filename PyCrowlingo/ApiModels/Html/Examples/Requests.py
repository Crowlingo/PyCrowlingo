from pydantic import BaseModel


class ExtractArticle(BaseModel):
    class Config:
        _url = "https://www.channelstv.com/2020/03/16/coronavirus-us-china-trade-blames-over-fear-mongering/"
        schema_extra = {
            "example": {
                "url": _url
            },
            "_python": [f"url = \"{_url}\"",
                        "client.html.extract_article(url)"]
        }
