from pydantic import BaseModel


class Search(BaseModel):
    class Config:
        _model_id = "japanese_faq"
        _text = 'Can I unregister as I am not in charge of class anymore ?'
        _variations = ["en", "ja"]
        schema_extra = {
            "example": {
                "text": _text,
                "variations": _variations
            },
            "_python": [f"model_id = \"{_model_id}\"", f"text = \"{_text}\"", f"variations = {_variations}",
                        "client.faq.search(model_id, text)"]
        }


class CreateQuestion(BaseModel):
    class Config:
        _model_id = "japanese_faq"
        _variations = {'en': "I'm no longer in charge of class, so I want to unregister.",
                       "ja": "授業担当者ではなくなったので登録解除したい。"}
        _answer_id = "HGBkrUrM"
        schema_extra = {
            "example": {
                "variations": _variations
            },
            "_python": [f"model_id = \"{_model_id}\"", f"variations = {_variations}",
                        f"answer_id = \"{_answer_id}\"",
                        "client.faq.create_question(model_id, variations, answer_id=answer_id)"]
        }


class CreateAnswer(BaseModel):
    class Config:
        _variations = {
            'en': "Even if you are not a regular student, you can use kibaco if you have been "
                  "issued a User ID for 'Information System for Educational Research'. If you "
                  "are a research student or special course student, and you have not "
                  "acquired this user ID, please apply first. In addition, the teacher in "
                  "charge of the class may apply for the class ID and may use the issued ID "
                  "for the audience and subjects who have taken courses.",
            "ja":
                '新学期が始まる約一ヶ月までの情報を基にしているので、それ以降の変更は反映されていません。授業担当者ではなくなった場合、登録を解除する必要があります。登録解除は '
                'システム管理室2（e-learning-ml●ml.tmu.ac.jp'
                '、●をアットマークに変えてください）宛てに申請メール（科目名、授業番号、解除する教員氏名、解除する教員の教育研究用情報システムID）を主担当教員からお送りいただくか、主担当教員をCC'
                'に入れてお送りいただく必要があります。'}
        _model_id = 'japanese_faq'
        schema_extra = {
            "example": {"model_id": _model_id, "variations": _variations},
            "_python": [f"model_id = \"{_model_id}\"", f"variations = {_variations}",
                        "client.faq.create_answer(model_id, variations)"]
        }


class DeleteModel(BaseModel):
    class Config:
        _model_id = "japanese_faq"
        schema_extra = {
            "_python": [f"model_id = \"{_model_id}\"",
                        "client.faq.delete_model(model_id)"]
        }


class DeleteQuestion(BaseModel):
    class Config:
        _model_id = "japanese_faq"
        _question_id = "GPcbbjvo"
        schema_extra = {
            "_python": [f"model_id = \"{_model_id}\"", f"question_id = \"{_question_id}\"",
                        "client.faq.delete_question(model_id, question_id)"]}


class DeleteAnswer(BaseModel):
    class Config:
        _model_id = "japanese_faq"
        _answer_id = "HGBkrUrM"
        schema_extra = {
            "_python": [f"model_id = \"{_model_id}\"", f"answer_id = \"{_answer_id}\"",
                        "client.faq.delete_answer(model_id, answer_id)"]
        }
