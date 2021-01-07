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


class CreateQuestions(BaseModel):
    class Config:
        _model_id = "japanese_faq"
        _questions = [{"variations": {'en': "I'm no longer in charge of class, so I want to unregister.",
                                        "ja": "授業担当者ではなくなったので登録解除したい。"},
                       "answer_id": "HGBkrUrM"
                       }]
        schema_extra = {
            "example": {
                "questions": _questions
            },
            "_python": [f"model_id = \"{_model_id}\"",
                        f"questions = {_questions}",
                        "client.faq.create_questions(model_id, questions)"]
        }


class CreateAnswers(BaseModel):
    class Config:
        _answers = [{"variations": {
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
        }]
        _model_id = 'japanese_faq'
        schema_extra = {
            "example": {"answers": _answers},
            "_python": [f"model_id = \"{_model_id}\"", f"answers = {_answers}",
                        "client.faq.create_answers(model_id, answers)"]
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


class UpdateQuestion(BaseModel):
    class Config:
        _model_id = "japanese_faq"
        _answer_id = "A11"
        _question_id = "GPcbbjvo"
        schema_extra = {
            "example": {
                "answer_id": _answer_id
            },
            "_python": [f"model_id = \"{_model_id}\"", f"question_id = \"{_question_id}\"",
                        f"answer_id = \"{_answer_id}\"",
                        "client.faq.update_question(model_id, question_id, answer_id=answer_id)"]
        }


class UpdateAnswer(BaseModel):
    class Config:
        _model_id = "japanese_faq"
        _variations = {"en": "Google it."}
        _answer_id = "HGBkrUrM"
        schema_extra = {
            "example": {
                "variations": _variations
            },
            "_python": [f"model_id = \"{_model_id}\"", f"answer_id = \"{_answer_id}\"",
                        f"variations = {_variations}",
                        "client.faq.update_answer(model_id, answer_id, variations=variations)"]
        }


class GetQuestion(BaseModel):
    class Config:
        _model_id = "japanese_faq"
        _question_id = "GPcbbjvo"
        schema_extra = {
            "_python": [f"model_id = \"{_model_id}\"", f"question_id = \"{_question_id}\""
                                                       "client.faq.get_question(model_id, question_id)"]
        }


class GetAnswer(BaseModel):
    class Config:
        _model_id = "japanese_faq"
        _answer_id = "HGBkrUrM"
        schema_extra = {
            "_python": [f"model_id = \"{_model_id}\"", f"answer_id = \"{_answer_id}\"",
                        "client.faq.get_answer(model_id, answer_id)"]
        }


class ListQuestions(BaseModel):
    class Config:
        _model_id = "japanese_faq"
        schema_extra = {
            "_python": [f"model_id = \"{_model_id}\"",
                        "client.faq.list_questions(model_id)"]
        }


class ListAnswers(BaseModel):
    class Config:
        _model_id = "japanese_faq"
        schema_extra = {
            "_python": [f"model_id = \"{_model_id}\"",
                        "client.faq.list_answers(model_id)"]
        }
