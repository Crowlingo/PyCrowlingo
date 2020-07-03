from pydantic import BaseModel


class Classify(BaseModel):
    class Config:
        schema_extra = {
            "example":
                {'classes': [{'class_id': 'Software Recommendation', 'confidence': 0.6562462150850555},
                             {'class_id': 'None', 'confidence': 0.1208982732456724},
                             {'class_id': 'Shutdown Computer', 'confidence': 0.10488410138625179},
                             {'class_id': 'Setup Printer', 'confidence': 0.09517660221370582},
                             {'class_id': 'Make Update', 'confidence': 0.022794808069314842}]}
        }


class CreateDocuments(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                "documents_id": ["PQk4AQbu"]
            }
        }


class DeleteDocument(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                "document_id": "PQk4AQbu"
            }
        }


class UpdateDocument(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                "document_id": "PQk4AQbu"
            }
        }


class GetDocument(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                "id": "PQk4AQbu",
                "text": "How to setup wireless printing from a printer connected via usb on Ubuntu Server 12.10?",
                "lang": "en",
                "class_id": "Setup Printer",
                "optional_features": {}
            }
        }


class ListDocuments(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                "documents": [{"id": "PQk4AQbu",
                               "text": "How to setup wireless printing from a printer connected via usb on Ubuntu "
                                       "Server 12.10?",
                               "lang": "en",
                               "class_id": "Setup Printer",
                               "optional_features": {}
                               }]
            }
        }
