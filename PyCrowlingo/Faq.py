from .Connector import Connector

from .ApiModels import Faq as Models


class Faq(Connector):

    def search(self, model_id, text, model_owner=None, lang=None, variations=None, prod_version=None, limit=None):
        return Models.Search.fill(**locals()).call(self.client)

    def create_questions(self, model_id, questions, model_owner=None):
        return Models.CreateQuestions.fill(**locals()).call(self.client)

    def create_answers(self, model_id, answers, model_owner=None):
        return Models.CreateAnswers.fill(**locals()).call(self.client)

    def update_question(self, model_id, question_id, model_owner=None, answer_id=None, variations=None):
        return Models.UpdateQuestion.fill(**locals()).call(self.client)

    def update_answer(self, model_id, answer_id, model_owner=None, variations=None):
        return Models.UpdateAnswer.fill(**locals()).call(self.client)

    def delete_question(self, model_id, question_id, model_owner=None):
        return Models.DeleteQuestion.fill(**locals()).call(self.client)

    def delete_answer(self, model_id, answer_id, model_owner=None):
        return Models.DeleteAnswer.fill(**locals()).call(self.client)

    def get_question(self, model_id, question_id, model_owner=None):
        return Models.GetQuestion.fill(**locals()).call(self.client)

    def get_answer(self, model_id, document_id, model_owner=None):
        return Models.GetAnswer.fill(**locals()).call(self.client)

    def list_questions(self, model_id, model_owner=None, page=None, page_size=None,
                       sort=None, ascending=None, id=None, answer_id=None):
        return Models.ListQuestions.fill(**locals()).call(self.client)

    def list_answers(self, model_id, model_owner=None, page=None, page_size=None, sort=None, ascending=None, id=None):
        return Models.ListAnswers.fill(**locals()).call(self.client)

    def upload_csv_questions(self, model_id, filename, model_owner=None,
                             fieldnames=None, delimiter=",", batch_size=200):
        from .FileUploader import upload_csv

        upload_csv(self.client, Models.CreateQuestions, "questions", **locals())

    def upload_csv_answers(self, model_id, filename, model_owner=None, fieldnames=None, delimiter=",", batch_size=200):
        from .FileUploader import upload_csv

        upload_csv(self.client, Models.CreateAnswers, "answers", **locals())

