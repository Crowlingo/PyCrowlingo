from pydantic import BaseModel


class Pipeline(BaseModel):
    class Config:
        schema_extra = {
            "example":
                {'responses': {'[POST] /v1/languages/detect': {
                    'languages_confidence': [{'code': 'en', 'name': 'anglais', 'confidence': 99.0}], 'sentences': [
                        {'languages_confidence': [{'code': 'en', 'name': 'anglais', 'confidence': 98.0}],
                         'text': 'On 26 April 1986, Chernobyl suffered the world’s worst nuclear disaster.', 'start': 0,
                         'end': 72}, {'languages_confidence': [{'code': 'en', 'name': 'anglais', 'confidence': 99.0}],
                                      'text': 'An experiment designed to test the safety of the power plant went '
                                              'wrong and caused a fire which spewed radiation for 10 days.',
                                      'start': 73, 'end': 198},
                        {'languages_confidence': [{'code': 'en', 'name': 'anglais', 'confidence': 99.0}],
                         'text': 'Clouds carrying radioactive particles drifted for thousands of miles, releasing '
                                 'toxic rain all over Europe.',
                         'start': 199, 'end': 306},
                        {'languages_confidence': [{'code': 'en', 'name': 'anglais', 'confidence': 98.0}],
                         'text': 'Those living close to Chernobyl - about 116,000 people - were immediately evacuated.',
                         'start': 307, 'end': 391},
                        {'languages_confidence': [{'code': 'en', 'name': 'anglais', 'confidence': 98.0}],
                         'text': 'A 30 km exclusion zone was imposed around the damaged reactor.', 'start': 392,
                         'end': 454}, {'languages_confidence': [{'code': 'en', 'name': 'anglais', 'confidence': 98.0}],
                                       'text': 'This was later expanded to cover more affected areas.', 'start': 455,
                                       'end': 508}]}, '[POST] /v1/entities/extract': {
                    'entities': [{'start': 3, 'end': 16, 'ent_type': 'DATE', 'text': '26 April 1986'},
                                 {'start': 18, 'end': 27, 'ent_type': 'GPE', 'text': 'Chernobyl'},
                                 {'start': 190, 'end': 197, 'ent_type': 'DATE', 'text': '10 days'},
                                 {'start': 249, 'end': 267, 'ent_type': 'QUANTITY', 'text': 'thousands of miles'},
                                 {'start': 299, 'end': 305, 'ent_type': 'LOC', 'text': 'Europe'},
                                 {'start': 329, 'end': 338, 'ent_type': 'GPE', 'text': 'Chernobyl'},
                                 {'start': 341, 'end': 354, 'ent_type': 'CARDINAL', 'text': 'about 116,000'},
                                 {'start': 394, 'end': 399, 'ent_type': 'QUANTITY', 'text': '30 km'}]}}}
        }
