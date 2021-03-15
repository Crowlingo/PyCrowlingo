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


# TODO insert real response

class RenameClass(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                'public': False, 'markers': [], 'description': None, 'name': 'AskUbuntu', 'versions': {'test': {
                    'metrics': {'micro': {'precision': 0.9333333333333333, 'recall': 0.9333333333333333,
                                          'f1': 0.9333333333333333},
                                'macro': {'precision': 0.7692307692307693, 'recall': 0.76, 'f1': 0.7611111111111111},
                                'weighted': {'precision': 0.9102564102564102, 'recall': 0.9333333333333333,
                                             'f1': 0.9175925925925925}}, 'version_id': 2}, 'prod': {
                    'metrics': {
                        'micro': {'precision': 0.9333333333333333, 'recall': 0.9333333333333333,
                                  'f1': 0.9333333333333333},
                        'macro': {'precision': 0.7692307692307693, 'recall': 0.76, 'f1': 0.7611111111111111},
                        'weighted': {'precision': 0.9102564102564102, 'recall': 0.9333333333333333,
                                     'f1': 0.9175925925925925}}, 'version_id': 2}}, 'category': 'classifier',
                'training_status': 'done', 'training_progress': 100, 'training_error': 'None',
                'training_start': '2020-11-14 10:55:41.506000', 'training_end': '2020-11-14 10:55:49.775000',
                'deploying_start': '2020-11-14 10:55:50.955000', 'deploying_end': '2020-11-14 10:55:51.121000',
                'owner': 'jonas.bouaziz@epita.fr', 'collaborators': {}, 'metadata': {
                    'classes': {'Shutdown Computer': 27, 'Software Recommendation': 57, 'OOS': 8, 'Setup Printer': 23,
                                'Make Update': 47}, 'markers': {}, 'documents': 162}

            }
        }
