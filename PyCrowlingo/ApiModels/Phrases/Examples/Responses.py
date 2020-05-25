from pydantic import BaseModel


class ExtractKeys(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                "key_phrases": [{"text": 'tomato sauce nozzle', "weigh": 0.031752697497046026},
                                {"text": 'sugary tomato sweetness', "weight": 0.02947166030985545},
                                {"text": 'oozy beefy mince', "weight": 0.028924779660601682},
                                {"text": 'savoury taste sensation', "weight": 0.02738701084630684},
                                {"text": 'humble meat pie', "weight": 0.0255610365121371},
                                {"text": 'young age', "weight": 0.018322040460932686},
                                {"text": 'hot climates', "weight": 0.017874783394024},
                                {"text": 'smallish hands', "weight": 0.017439467504265758},
                                {"text": 'shape mid-bite', "weight": 0.017103805586533544},
                                {"text": 'wintry days', "weight": 0.01667938878386825}]
            }
        }


class Match(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                "matches": [{'dist': 0.8634273409843445, 'end': 13, 'start': 6, 'text': 'mon ami'}]
            }
        }


class RuleBasedMatch(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                'matches': {'Get order reference': [{'start': 48, 'end': 60, 'text': 'pedido HS76R'}]},
                'visualization': None
            }
        }
