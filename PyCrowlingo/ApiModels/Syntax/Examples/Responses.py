from pydantic import BaseModel


class Extract(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                "sentences": [{"start": 0, "end": 16,
                               "words": [{"start": 0, "end": 5, "id": 0, "text": 'There', "pos_tag": 'PRON',
                                          "lemma": 'there', "dep": 'expl', "head": 1, "feats": {}},
                                         {"start": 6, "end": 10, "id": 1, "text": 'were', "pos_tag": 'VERB',
                                          "lemma": 'be', "dep": 'ROOT', "head": 1, "feats": {}},
                                         {"start": 11, "end": 17, "id": 2, "text": 'things', "pos_tag": 'NOUN',
                                          "lemma": 'thing', "dep": 'nsubj', "head": 1, "feats": {}},
                                         {"start": 18, "end": 20, "id": 3, "text": 'in', "pos_tag": 'ADP',
                                          "lemma": 'in', "dep": 'case', "head": 5, "feats": {}},
                                         {"start": 21, "end": 24, "id": 4, "text": 'the', "pos_tag": 'DET',
                                          "lemma": 'the', "dep": 'det', "head": 5, "feats": {}},
                                         {"start": 25, "end": 32, "id": 5, "text": 'shadows', "pos_tag": 'NOUN',
                                          "lemma": 'shadows', "dep": 'nmod', "head": 2, "feats": {}},
                                         {"start": 32, "end": 33, "id": 6, "text": ';', "pos_tag": 'PUNCT',
                                          "lemma": ';', "dep": 'punct', "head": 1, "feats": {}},
                                         {"start": 34, "end": 35, "id": 7, "text": 'a', "pos_tag": 'DET',
                                          "lemma": 'a', "dep": 'det', "head": 9, "feats": {}},
                                         {"start": 36, "end": 41, "id": 8, "text": 'metal', "pos_tag": 'NOUN',
                                          "lemma": 'metal', "dep": 'compound', "head": 9, "feats": {}},
                                         {"start": 42, "end": 46, "id": 9, "text": 'pail', "pos_tag": 'NOUN',
                                          "lemma": 'pail', "dep": 'nsubj', "head": 1, "feats": {}},
                                         {"start": 46, "end": 47, "id": 10, "text": ',', "pos_tag": 'PUNCT',
                                          "lemma": ',', "dep": 'punct', "head": 9, "feats": {}},
                                         {"start": 48, "end": 49, "id": 11, "text": 'a', "pos_tag": 'DET',
                                          "lemma": 'a', "dep": 'det', "head": 12, "feats": {}},
                                         {"start": 50, "end": 53, "id": 12, "text": 'mop', "pos_tag": 'NOUN',
                                          "lemma": 'mop', "dep": 'appos', "head": 9, "feats": {}},
                                         {"start": 53, "end": 54, "id": 13, "text": ',', "pos_tag": 'PUNCT',
                                          "lemma": ',', "dep": 'punct', "head": 12, "feats": {}},
                                         {"start": 55, "end": 59, "id": 14, "text": 'rags', "pos_tag": 'NOUN',
                                          "lemma": 'rag', "dep": 'appos', "head": 12, "feats": {}},
                                         {"start": 59, "end": 60, "id": 15, "text": '.', "pos_tag": 'PUNCT',
                                          "lemma": '.', "dep": 'punct', "head": 1, "feats": {}}]}],
                "visualization": None
            }
        }
