from pydantic import BaseModel


class Get(BaseModel):
    class Config:
        schema_extra = {
            "example":
                {"name": "AskUbuntu",
                 "category": "classifier",
                 "training_status": "done",
                 "owner": "john@crowlingo.com",
                 "deployed": True,
                 "metrics": {},
                 "collaborators": {}}
        }


class Train(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                "model_id": "AskUbuntu"
            }
        }


class Deploy(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                "model_id": "AskUbuntu"
            }
        }


class Clear(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                "model_id": "AskUbuntu"
            }
        }


class Delete(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                "model_id": "AskUbuntu"
            }
        }


class AddCollaborator(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                "collaborator": "john@crowlingo.com"
            }
        }


class RemoveCollaborator(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                "collaborator": "john@crowlingo.com"
            }
        }


# TODO insert real response

class Edit(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                'public': False, 'markers': [], 'description': 'Best model ever', 'name': 'AskUbuntu', 'versions': {
                    'test': {'metrics': {'micro': {'precision': 0.9333333333333333, 'recall': 0.9333333333333333,
                                                   'f1': 0.9333333333333333},
                                         'macro': {'precision': 0.7692307692307693, 'recall': 0.76,
                                                   'f1': 0.7611111111111111},
                                         'weighted': {'precision': 0.9102564102564102, 'recall': 0.9333333333333333,
                                                      'f1': 0.9175925925925925}}, 'version_id': 2}, 'prod': {
                        'metrics': {'micro': {'precision': 0.9333333333333333, 'recall': 0.9333333333333333,
                                              'f1': 0.9333333333333333},
                                    'macro': {'precision': 0.7692307692307693, 'recall': 0.76,
                                              'f1': 0.7611111111111111},
                                    'weighted': {'precision': 0.9102564102564102, 'recall': 0.9333333333333333,
                                                 'f1': 0.9175925925925925}}, 'version_id': 2}},
                'category': 'classifier', 'training_status': 'done', 'training_progress': 100,
                'training_error': 'None', 'training_start': '2020-11-14 10:55:41.506000',
                'training_end': '2020-11-14 10:55:49.775000', 'deploying_start': '2020-11-14 10:55:50.955000',
                'deploying_end': '2020-11-14 10:55:51.121000', 'owner': 'jonas.bouaziz@epita.fr', 'collaborators': {},
                'metadata': {
                    'classes': {'Shutdown Computer': 27, 'Software Recommendation': 57, 'OOS': 8, 'Setup Printer': 23,
                                'Make Update': 47}, 'markers': {}, 'documents': 162}}
        }


class ListPublic(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                'models': [{'public': True, 'markers': [], 'description': 'Best model ever', 'name': 'AskUbuntu',
                            'versions': {'test': {'metrics': {
                                'micro': {'precision': 0.9333333333333333, 'recall': 0.9333333333333333,
                                          'f1': 0.9333333333333333},
                                'macro': {'precision': 0.7692307692307693, 'recall': 0.76, 'f1': 0.7611111111111111},
                                'weighted': {'precision': 0.9102564102564102, 'recall': 0.9333333333333333,
                                             'f1': 0.9175925925925925}}, 'version_id': 2}, 'prod':
                                {'metrics': {
                                    'micro': {'precision': 0.9333333333333333, 'recall': 0.9333333333333333,
                                              'f1': 0.9333333333333333},
                                    'macro': {'precision': 0.7692307692307693, 'recall': 0.76,
                                              'f1': 0.7611111111111111},
                                    'weighted': {'precision': 0.9102564102564102, 'recall': 0.9333333333333333,
                                                 'f1': 0.9175925925925925}}, 'version_id': 2}},
                            'category': 'classifier',
                            'training_status': 'done', 'training_progress': 100, 'training_error': 'None',
                            'training_start': '2020-11-14 10:55:41.506000',
                            'training_end': '2020-11-14 10:55:49.775000',
                            'deploying_start': '2020-11-14 10:55:50.955000',
                            'deploying_end': '2020-11-14 10:55:51.121000', 'owner': 'jonas.bouaziz@epita.fr',
                            'collaborators': {}, 'metadata': {
                        'classes': {'Shutdown Computer': 27, 'Software Recommendation': 57, 'OOS': 8,
                                    'Setup Printer': 23, 'Make Update': 47}, 'markers': {}, 'documents': 162}}]}
        }


class ListUser(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                'models': [{'public': True, 'markers': [], 'description': 'Best model ever', 'name': 'AskUbuntu',
                            'versions': {'test': {'metrics': {
                                'micro': {'precision': 0.9333333333333333, 'recall': 0.9333333333333333,
                                          'f1': 0.9333333333333333},
                                'macro': {'precision': 0.7692307692307693, 'recall': 0.76, 'f1': 0.7611111111111111},
                                'weighted': {'precision': 0.9102564102564102, 'recall': 0.9333333333333333,
                                             'f1': 0.9175925925925925}}, 'version_id': 2}, 'prod': {
                                'metrics': {
                                    'micro': {'precision': 0.9333333333333333, 'recall': 0.9333333333333333,
                                              'f1': 0.9333333333333333},
                                    'macro': {'precision': 0.7692307692307693, 'recall': 0.76,
                                              'f1': 0.7611111111111111},
                                    'weighted': {'precision': 0.9102564102564102, 'recall': 0.9333333333333333,
                                                 'f1': 0.9175925925925925}}, 'version_id': 2}},
                            'category': 'classifier',
                            'training_status': 'done', 'training_progress': 100, 'training_error': 'None',
                            'training_start': '2020-11-14 10:55:41.506000',
                            'training_end': '2020-11-14 10:55:49.775000',
                            'deploying_start': '2020-11-14 10:55:50.955000',
                            'deploying_end': '2020-11-14 10:55:51.121000', 'owner': 'jonas.bouaziz@epita.fr',
                            'collaborators': {}, 'metadata': {
                        'classes': {'Shutdown Computer': 27, 'Software Recommendation': 57, 'OOS': 8,
                                    'Setup Printer': 23, 'Make Update': 47}, 'markers': {}, 'documents': 162}},
                           {'public': False, 'markers': [], 'description': None, 'name': 'japanese_faq',
                            'versions': {'test': {'metrics': None, 'version_id': 2},
                                         'prod': {'metrics': None, 'version_id': 2}}, 'category': 'faq',
                            'training_status': 'done', 'training_progress': 100, 'training_error': 'None',
                            'training_start': '2020-11-14 11:22:41.257000',
                            'training_end': '2020-11-14 11:22:57.117000',
                            'deploying_start': '2020-11-14 11:23:00.251000',
                            'deploying_end': '2020-11-14 11:23:11.684000', 'owner': 'jonas.bouaziz@epita.fr',
                            'collaborators': {},
                            'metadata': {'questions_markers': {}, 'answers_markers': {}, 'questions': 427,
                                         'answers': 79}}]
            }
        }
