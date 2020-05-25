from pydantic import BaseModel


class Extract(BaseModel):
    class Config:
        _text = "Australia is being ravaged by the worst wildfires seen in decades, with large swaths of the country " \
                "devastated since the fire season began in late July. At least 28 people have died nationwide, " \
                "and in the state of New South Wales (NSW) alone, more than 3,000 homes have been destroyed or " \
                "damaged. State and federal authorities are struggling to contain the massive blazes, " \
                "even with firefighting assistance from other countries, including the United States. All this has " \
                "been exacerbated by persistent heat and drought, and many point to climate change as a factor making " \
                "natural disasters go from bad to worse. There have been fires in every Australian state, " \
                "but New South Wales has been hardest hit. Blazes have torn through bushland, wooded areas, " \
                "and national parks like the Blue Mountains. Some of Australia's largest cities have also been " \
                "affected, including Melbourne and Sydney -- where fires have damaged homes in the outer suburbs and " \
                "thick plumes of smoke have blanketed the urban center. Earlier in December, the smoke was so bad in " \
                "Sydney that air quality measured 11 times the hazardous level. The fires range in area from small " \
                "blazes -- isolated buildings or part of a neighborhood -- to massive infernos that occupy entire " \
                "hectares of land. Some start and are contained in a matter of days, but the biggest blazes have been " \
                "burning for months. In NSW alone, more than 100 fires are still burning. "

        schema_extra = {
            "example": {
                "text": _text
            },
            "_python": [f"text = \"{_text}\"",
                        "client.summary.extract(text)"]

        }
