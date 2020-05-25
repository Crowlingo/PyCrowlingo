from pydantic import BaseModel


class ExtractKeys(BaseModel):
    class Config:
        _text = "If you ever wondered why Australians have such an obsession with the humble meat pie, " \
                "this inculcation from a very young age is possibly at the heart of it. In heater-less schools built " \
                "for hot climates despite wintry days, there was nothing quite like the smell and savoury taste " \
                "sensation found in this warm, mince-filled bakery delight. It came in just the right size for two " \
                "smallish hands to hold, with a square casing solid enough to retain its shape mid-bite. The pastry " \
                "on top was wonderfully flaky, but flimsy too, so the tomato sauce nozzle could be poked directly " \
                "into the pie, mixing sugary tomato sweetness with oozy beefy mince.. "
        schema_extra = {
            "example": {
                "text": _text
            },
            "_python": [f"text = \"{_text}\"",
                        "client.phrases.extract_keys(text)"]
        }


class Match(BaseModel):
    class Config:
        _text = "Salut mon ami !"
        _phrase = "my friend"
        schema_extra = {
            "example":
                {"text": _text,
                 "phrase": _phrase},
            "_python": [f"text = \"{_text}\"", f"phrase = \"{_phrase}\"",
                        "client.phrases.match(model_id, phrase)"]
        }


class RuleBasedMatch(BaseModel):
    class Config:
        _text = "Hola, todavía no he recibido una factura por mi pedido HS76R. ¿Puedes decirme cuándo se supone que " \
                "debo tenerlo? Gracias​ "
        _patterns = {"Get order reference": f'text="pedido" text~"HS[a-zA-Z0-9]*"'}
        schema_extra = {
            "example":
                {"text": _text,
                 "patterns": _patterns},
            "_python": [f"text = \"{_text}\"", f"patterns = \"{_patterns}\"",
                        "client.phrases.rule_based_match(text, patterns)"]
        }