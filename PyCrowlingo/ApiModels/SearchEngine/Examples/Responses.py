from pydantic import BaseModel


class Search(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                'keywords': {'ar': [{'weight': 0.7677102857491178, 'text': 'الهجوم'}],
                             'en': [{'weight': 1.0000002384185933, 'text': 'attack'}],
                             'es': [{'weight': 0.8562676777810339, 'text': 'ataque'}],
                             'ca': [{'weight': 0.7647217495531464, 'text': 'atac'}],
                             'fr': [{'weight': 0.8971692096572639, 'text': 'attaque'}]}
            }
        }


class CreateDocuments(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                "documents_id": ["jLcbfzso"]
            }
        }


class CreateKeywords(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                "documents_id": ["MPzvfqgK"]
            }
        }


class DeleteDocuments(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                "documents_id": ["jLcbfzso"]
            }
        }
