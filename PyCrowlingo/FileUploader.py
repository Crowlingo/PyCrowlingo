import csv, sys
csv.field_size_limit(sys.maxsize)

def upload_csv(client, function, function_field, filename, fieldnames=None, batch_size=200, delimiter=',', **kwargs):
    def check_batch(force=False):
        if len(docs) >= batch_size or force:
            res.append([e for e in function.fill(**kwargs, **{function_field: docs}).call(client)])
            docs.clear()

    res = []
    docs = []
    with open(filename) as f:
        for doc in csv.DictReader(f, fieldnames, delimiter=delimiter):
            docs.append(doc)
            check_batch()
        check_batch(True)
        return res
