from .Connector import Connector

from .ApiModels import SearchEngine as Models


class SearchEngine(Connector):

    def search(self, model_id, text, limit=None, languages=None, precision=None, include_query=None):
        return Models.Search.fill(**locals()).call(self.client)

    def create_documents(self, model_id, documents, light=None):
        return Models.CreateDocuments.fill(**locals()).call(self.client)

    def create_keywords(self, model_id, keywords):
        return Models.CreateKeywords.fill(**locals()).call(self.client)

    def delete_documents(self, model_id, documents_id):
        return Models.DeleteDocuments.fill(**locals()).call(self.client)

    def wait_indexing(self, model_id, time_sleep=3):
        import time
        from tqdm import tqdm

        metadata = self.client.model.get(model_id).metadata
        pending = metadata.get("pending")
        indexed = sum(metadata.get("languages", {}).values())
        total = pending
        with tqdm(total=total) as pbar:
            while pending:
                time.sleep(time_sleep)
                metadata = self.client.model.get(model_id).metadata
                new_pending = metadata.get("pending")
                new_indexed = sum(metadata.get("languages", {}).values())
                treated = new_indexed - indexed
                added = new_pending - pending + treated
                total += added
                pbar.update(treated)
                pbar.total = total
                pbar.refresh()
                pending = new_pending
                indexed = new_indexed
        return metadata.get("languages")
