from pydantic import BaseModel


class Extract(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                'entities': [
                    {
                        "start": 0,
                        "end": 5,
                        "ent_type": "PERSON",
                        "text": "Trump"
                    },
                    {
                        "start": 57,
                        "end": 67,
                        "ent_type": "FAC",
                        "text": "Mar-a-Lago"
                    },
                    {
                        "start": 78,
                        "end": 85,
                        "ent_type": "GPE",
                        "text": "Florida"
                    },
                    {
                        "start": 123,
                        "end": 128,
                        "ent_type": "ORG",
                        "text": "House"
                    },
                    {
                        "start": 161,
                        "end": 171,
                        "ent_type": "DATE",
                        "text": "a week ago"
                    },
                    {
                        "start": 177,
                        "end": 187,
                        "ent_type": "NORP",
                        "text": "Democratic"
                    },
                    {
                        "start": 192,
                        "end": 197,
                        "ent_type": "ORG",
                        "text": "House"
                    },
                    {
                        "start": 198,
                        "end": 207,
                        "ent_type": "DATE",
                        "text": "last week"
                    },
                    {
                        "start": 279,
                        "end": 287,
                        "ent_type": "ORG",
                        "text": "Congress"
                    },
                    {
                        "start": 322,
                        "end": 329,
                        "ent_type": "GPE",
                        "text": "Ukraine"
                    }
                ]
            }
        }


class Duckling(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                "duckling": [
                    {
                        "body": "On 26 April 1986",
                        "start": 0,
                        "value": {
                            "value": "1986-04-26T00:00:00.000-08:00",
                            "grain": "day",
                            "type": "value"
                        },
                        "end": 16,
                        "dim": "time",
                        "latent": False
                    },
                    {
                        "body": "10 days",
                        "start": 190,
                        "value": {
                            "value": 10,
                            "day": 10,
                            "type": "value",
                            "unit": "day",
                            "normalized": {
                                "value": 864000,
                                "unit": "second"
                            }
                        },
                        "end": 197,
                        "dim": "duration",
                        "latent": False
                    },
                    {
                        "body": "thousands",
                        "start": 249,
                        "value": {
                            "value": 1000,
                            "type": "value"
                        },
                        "end": 258,
                        "dim": "number",
                        "latent": False
                    },
                    {
                        "body": "116,000",
                        "start": 347,
                        "value": {
                            "value": 116000,
                            "type": "value"
                        },
                        "end": 354,
                        "dim": "number",
                        "latent": False
                    },
                    {
                        "body": "immediately",
                        "start": 369,
                        "value": {
                            "value": "2020-05-23T04:29:29.863-07:00",
                            "grain": "second",
                            "type": "value"
                        },
                        "end": 380,
                        "dim": "time",
                        "latent": False
                    },
                    {
                        "body": "30 km",
                        "start": 394,
                        "value": {
                            "value": 30,
                            "type": "value",
                            "unit": "kilometre"
                        },
                        "end": 399,
                        "dim": "distance",
                        "latent": False
                    }
                ]
            }
        }
