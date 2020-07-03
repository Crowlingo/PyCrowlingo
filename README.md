# PyCrowlingo: Python SDK for Crowlingo APIs

Here is the official Python client for [Crowlingo](https://crowlingo.com). Access to all NLP and NLU services that analyze texts regardless of the language.
  


Installation
---------------


You can use pip to install the library:

```bash
$ pip install PyCrowlingo
```

Alternatively, you can just clone the repository and run the setup.py script:

```bash
$ python setup.py install
```


Usage
------

First of all, you will need to instantiate a client of Crowlingo. You can do it using your API token:   

```python
from PyCrowlingo import Client
client = Client('[TOKEN]')
```

Or using your account credentials:

 ```python
from PyCrowlingo import Client
client = Client(username='[EMAIL]', password='[PASSWORD]')
```

### QuickStart

You can call all the endpoints available on Crowlingo. All of them are detailed with examples on [the documentation](https://crowlingo.com/docs). 


```python
text = "Est-il recommandé d'utiliser MongoDb pour indexer mes documents ?"
res = client.languages.detect(text)
print(res)
# => Detect(sentences=[Sentence(start=0, end=65, languages_confidence=[ConfidenceLang(name='French', code='fr', confidence=98.0)], text="Est-il recommandé d'utiliser MongoDb pour indexer mes documents ?")], languages_confidence=[ConfidenceLang(name='French', code='fr', confidence=98.0)])

```

The response will be [Pydantic](https://github.com/samuelcolvin/pydantic) object.
So, you can get the values with the response's attributes:  

```python
print(client.languages.detect(text).languages_confidence)
# =>  '[ConfidenceLang(name='French', code='fr', confidence=98.0)]'
```

### Pipeline

If you need to analyze texts through different services, it can be cumbersome to call the API for every step of processing.
Gain some speed and productivity by using a Pipeline. It allows you to create a workflow of processing for your data.
To do so, you have to use the ApiModels instead of the client function.

```python
from PyCrowlingo import Pipeline
from PyCrowlingo.ApiModels import *
text = "On 26 April 1986, Chernobyl suffered the world’s worst nuclear disaster. An experiment designed to test the safety of the power plant went wrong and caused a fire which spewed radiation for 10 days. Clouds carrying radioactive particles drifted for thousands of miles, releasing toxic rain all over Europe. Those living close to Chernobyl - about 116,000 people - were immediately evacuated. A 30 km exclusion zone was imposed around the damaged reactor. This was later expanded to cover more affected areas."
pipeline = Pipeline(client, text=text) 
# Put the client on the pipeline and the common variables using keywords arguments
pipeline.add(Concepts.Extract, precision=0.9).add(Entities.Extract, visualize=True).add(Entities.Duckling)
# Add each step using pipeline.add(EndpointModel, *individuals arguments)
res = pipeline.call()
# Execute the pipeline
print(res)
# => responses={'[POST] /entities/duckling': {'duckling': [{'body': 'On 26 April 1986', 'start': 0, 'value': {'values': [{'value': '1986-04-26T00:00:00.000-08:00', 'grain': 'day', 'type': 'value'}], 'value': '1986-04-26T00:00:00.000-08:00', 'grain': 'day', 'type': 'value'}, 'end': 16, 'dim': 'time', 'latent': False}, {'body': '10 days', 'start': 190, 'value': {'value': 10, 'day': 10, 'type': 'value', 'unit': 'day', 'normalized': {'value': 864000, 'unit': 'second'}}, 'end': 197, 'dim': 'duration', 'latent': False}, {'body': 'thousands', 'start': 249, 'value': {'value': 1000, 'type': 'value'}, 'end': 258, 'dim': 'number', 'latent': False}, {'body': '116,000', 'start': 347, 'value': {'value': 116000, 'type': 'value'}, 'end': 354, 'dim': 'number', 'latent': False}, {'body': 'immediately', 'start': 369, 'value': {'values': [{'value': '2020-05-25T15:57:30.724-07:00', 'grain': 'second', 'type': 'value'}], 'value': '2020-05-25T15:57:30.724-07:00', 'grain': 'second', 'type': 'value'}, 'end': 380, 'dim': 'time', 'latent': False}, {'body': '30 km', 'start': 394, 'value': {'value': 30, 'type': 'value', 'unit': 'kilometre'}, 'end': 399, 'dim': 'distance', 'latent': False}]}, '[POST] /entities/extract': {'entities': [{'start': 3, 'end': 16, 'ent_type': 'DATE', 'text': '26 April 1986'}, {'start': 18, 'end': 27, 'ent_type': 'GPE', 'text': 'Chernobyl'}, {'start': 190, 'end': 197, 'ent_type': 'DATE', 'text': '10 days'}, {'start': 249, 'end': 267, 'ent_type': 'QUANTITY', 'text': 'thousands of miles'}, {'start': 299, 'end': 305, 'ent_type': 'LOC', 'text': 'Europe'}, {'start': 329, 'end': 338, 'ent_type': 'GPE', 'text': 'Chernobyl'}, {'start': 341, 'end': 354, 'ent_type': 'CARDINAL', 'text': 'about 116,000'}, {'start': 394, 'end': 399, 'ent_type': 'QUANTITY', 'text': '30 km'}], 'visualization': '<div class="entities" style="line-height: 2.5; direction: ltr">On \n<mark class="entity" style="background: #bfe1d9; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em;">\n    26 April 1986\n    <span style="font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; text-transform: uppercase; vertical-align: middle; margin-left: 0.5rem">DATE</span>\n</mark>\n, \n<mark class="entity" style="background: #feca74; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em;">\n    Chernobyl\n    <span style="font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; text-transform: uppercase; vertical-align: middle; margin-left: 0.5rem">GPE</span>\n</mark>\n suffered the world’s worst nuclear disaster. An experiment designed to test the safety of the power plant went wrong and caused a fire which spewed radiation for \n<mark class="entity" style="background: #bfe1d9; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em;">\n    10 days\n    <span style="font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; text-transform: uppercase; vertical-align: middle; margin-left: 0.5rem">DATE</span>\n</mark>\n. Clouds carrying radioactive particles drifted for \n<mark class="entity" style="background: #e4e7d2; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em;">\n    thousands of miles\n    <span style="font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; text-transform: uppercase; vertical-align: middle; margin-left: 0.5rem">QUANTITY</span>\n</mark>\n, releasing toxic rain all over \n<mark class="entity" style="background: #ff9561; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em;">\n    Europe\n    <span style="font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; text-transform: uppercase; vertical-align: middle; margin-left: 0.5rem">LOC</span>\n</mark>\n. Those living close to \n<mark class="entity" style="background: #feca74; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em;">\n    Chernobyl\n    <span style="font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; text-transform: uppercase; vertical-align: middle; margin-left: 0.5rem">GPE</span>\n</mark>\n - \n<mark class="entity" style="background: #e4e7d2; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em;">\n    about 116,000\n    <span style="font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; text-transform: uppercase; vertical-align: middle; margin-left: 0.5rem">CARDINAL</span>\n</mark>\n people - were immediately evacuated. A \n<mark class="entity" style="background: #e4e7d2; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em;">\n    30 km\n    <span style="font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; text-transform: uppercase; vertical-align: middle; margin-left: 0.5rem">QUANTITY</span>\n</mark>\n exclusion zone was imposed around the damaged reactor. This was later expanded to cover more affected areas.</div>'}, '[POST] /concepts/extract': {'concepts': [{'id': 'Q129677', 'weight': 0.19254024269693001, 'labels': [{'text': 'Chernobyl', 'mentions': [{'start': 18, 'end': 27}, {'start': 329, 'end': 338}]}]}, {'id': 'Q11448', 'weight': 0.13384788867053848, 'labels': [{'text': 'radioactive', 'mentions': [{'start': 215, 'end': 226}]}, {'text': 'radiation', 'mentions': [{'start': 176, 'end': 185}]}]}, {'id': 'Q46', 'weight': 0.11258210752213413, 'labels': [{'text': 'Europe', 'mentions': [{'start': 299, 'end': 305}]}]}, {'id': 'Q274160', 'weight': 0.07002172766602058, 'labels': [{'text': 'toxic', 'mentions': [{'start': 279, 'end': 284}]}]}, {'id': 'Q7925', 'weight': 0.06886892370214791, 'labels': [{'text': 'rain', 'mentions': [{'start': 285, 'end': 289}]}]}, {'id': 'Q101965', 'weight': 0.06562043143894636, 'labels': [{'text': 'experiment', 'mentions': [{'start': 76, 'end': 86}]}]}, {'id': 'Q3196', 'weight': 0.06482017292518794, 'labels': [{'text': 'fire', 'mentions': [{'start': 158, 'end': 162}]}]}, {'id': 'Q356936', 'weight': 0.06390318225879862, 'labels': [{'text': 'exclusion zone', 'mentions': [{'start': 400, 'end': 414}]}]}, {'id': 'Q486', 'weight': 0.06317545950269358, 'labels': [{'text': 'nuclear disaster', 'mentions': [{'start': 55, 'end': 71}]}, {'text': 'disaster', 'mentions': []}]}, {'id': 'Q11369', 'weight': 0.057931103203040506, 'labels': [{'text': 'particles', 'mentions': [{'start': 227, 'end': 236}]}]}, {'id': 'Q8074', 'weight': 0.05530684102502764, 'labels': [{'text': 'Clouds', 'mentions': [{'start': 199, 'end': 205}]}]}, {'id': 'Q11573', 'weight': 0.05138191938853427, 'labels': [{'text': 'km', 'mentions': [{'start': 397, 'end': 399}]}]}]}}
print(res.responses[Entities.Extract.eid()])
# => {'entities': [{'start': 3, 'end': 16, 'ent_type': 'DATE', 'text': '26 April 1986'}, {'start': 18, 'end': 27, 'ent_type': 'GPE', 'text': 'Chernobyl'}, {'start': 190, 'end': 197, 'ent_type': 'DATE', 'text': '10 days'}, {'start': 249, 'end': 267, 'ent_type': 'QUANTITY', 'text': 'thousands of miles'}, {'start': 299, 'end': 305, 'ent_type': 'LOC', 'text': 'Europe'}, {'start': 329, 'end': 338, 'ent_type': 'GPE', 'text': 'Chernobyl'}, {'start': 341, 'end': 354, 'ent_type': 'CARDINAL', 'text': 'about 116,000'}, {'start': 394, 'end': 399, 'ent_type': 'QUANTITY', 'text': '30 km'}], 'visualization': '<div class="entities" style="line-height: 2.5; direction: ltr">On \n<mark class="entity" style="background: #bfe1d9; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em;">\n    26 April 1986\n    <span style="font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; text-transform: uppercase; vertical-align: middle; margin-left: 0.5rem">DATE</span>\n</mark>\n, \n<mark class="entity" style="background: #feca74; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em;">\n    Chernobyl\n    <span style="font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; text-transform: uppercase; vertical-align: middle; margin-left: 0.5rem">GPE</span>\n</mark>\n suffered the world’s worst nuclear disaster. An experiment designed to test the safety of the power plant went wrong and caused a fire which spewed radiation for \n<mark class="entity" style="background: #bfe1d9; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em;">\n    10 days\n    <span style="font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; text-transform: uppercase; vertical-align: middle; margin-left: 0.5rem">DATE</span>\n</mark>\n. Clouds carrying radioactive particles drifted for \n<mark class="entity" style="background: #e4e7d2; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em;">\n    thousands of miles\n    <span style="font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; text-transform: uppercase; vertical-align: middle; margin-left: 0.5rem">QUANTITY</span>\n</mark>\n, releasing toxic rain all over \n<mark class="entity" style="background: #ff9561; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em;">\n    Europe\n    <span style="font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; text-transform: uppercase; vertical-align: middle; margin-left: 0.5rem">LOC</span>\n</mark>\n. Those living close to \n<mark class="entity" style="background: #feca74; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em;">\n    Chernobyl\n    <span style="font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; text-transform: uppercase; vertical-align: middle; margin-left: 0.5rem">GPE</span>\n</mark>\n - \n<mark class="entity" style="background: #e4e7d2; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em;">\n    about 116,000\n    <span style="font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; text-transform: uppercase; vertical-align: middle; margin-left: 0.5rem">CARDINAL</span>\n</mark>\n people - were immediately evacuated. A \n<mark class="entity" style="background: #e4e7d2; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em;">\n    30 km\n    <span style="font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; text-transform: uppercase; vertical-align: middle; margin-left: 0.5rem">QUANTITY</span>\n</mark>\n exclusion zone was imposed around the damaged reactor. This was later expanded to cover more affected areas.</div>'}

# EndpointModel.ied() returns the id of endpoint which is used in the response 
```


### Bulk Request

Most of the time, you will need to apply this process on a dataset. Again, you will gain speed by using bulk request. It allows to perform many operations in the same time. 
Here is an example on how to do it:

```python
from PyCrowlingo import Bulk, Pipeline
from PyCrowlingo.ApiModels import *
text = "Est-il recommandé d'utiliser MongoDb pour indexer mes documents ?"
pipelines = [Pipeline().add(Languages.Detect, text=text)] * 300
res = Bulk(client, pipelines).call()
assert len(res.responses) == 300 # True
```

You can also do it in an iterative way:
```python
from PyCrowlingo import Bulk, Pipeline
from PyCrowlingo.ApiModels import *
text = "Est-il recommandé d'utiliser MongoDb pour indexer mes documents ?"
bulk = Bulk(client)
for i in range(300):
    bulk.add(Pipeline().add(Languages.Detect, text=text))
res = bulk.call()
assert len(res.responses) == 300 # True
```

Using a bulk will automatically make API requests using batch (you can controle its size using `batch_size` argument). So that, you don't have to worry about the management of the query size.

## Errors

Sometimes, you may face error when you call an endpoint. Every errors are identifiable by their ID. 
It can be easily managed on a pythonic way:

```python
from PyCrowlingo.Errors import ModelNotFound, CrowlingoException

model_id = "AskUbuntu"
try:
    client.classifier.clear_model(model_id)
except ModelNotFound:
    client.classifier.create_model(model_id)
except CrowlingoException as e:
    print(e)
``` 
Here is the list of available exceptions:
|Class | Error ID | Status code | Description|
|---|---|---|---|
TrainingError | TRAINING_ERROR | 400 | An error happened during the training
TokenNotFound |TOKEN_NOT_FOUND | 401 | Token not found. Insert your token in the query parameter with api_key=[YOUR_TOKEN] or in the headers with x-api-key:[YOUR TOKEN].
BadCredentials |BAD_CREDENTIALS | 401 | Could not validate credentials. Their might be an error in your token or email/password. Maybe your account has been disabled. Please contact us if you do not understand the reason.
TestModelForbidden | TEST_MODEL_FORBIDDEN | 403 | You do not have access to the test version of this model. Ask the access to the owner of the model or use the prod version of this model.
BadModelsPerms | BAD_MODELS_PERMS | 403 | You do not have the permissions to perform this action on this model. Ask for the owner of this model to provides you more rights.
BadModelCategory | BAD_MODEL_CATEGORY | 404 | This model cannot be use for this kind of request. Create a new model or use another endpoint.
ModelNotDeployed |MODEL_NOT_DEPLOYED | 404 | This model is not deployed. Use the test model or deploy it first.
CollaboratorNotFound | COLLABORATOR_NOT_FOUND | 404 | This collaborator was not found. Maybe it has already delete the model or you did not add it as collaborator on this model.
ModelNotFound | MODEL_NOT_FOUND | 404 | We cannot find a model with this id. You have to create a model before using it.
DocumentNotFound | DOCUMENT_NOT_FOUND | 404 | We cannot find a document with this id. You have to create a document before using it.
DuplicateModelId | DUPLICATE_MODEL_ID | 409 |You already have a model with this id, please delete the model first if you want to overwrite it or use the endpoint update to create a new version of this model.
ContentLengthRequired | CONTENT_LENGTH_REQUIRED | 411 |You need to provide a content length header for POST and PATCH requests.
RequestEntityTooLarge | REQUEST_ENTITY_TOO_LARGE | 413 |The payload of your body is too large. Try to split your request with smaller payload.
BadParametersQuery | BAD_PARAMETERS_QUERY | 422 |The parameters of the query do not correspond to the documentation description. The query cannot be processed.
ModelNotTrained | MODEL_NOT_TRAINED | 423 | This model is not trained yet. You have to wait until it is trained or run the training before performing this action.
MinuteLimitReached | MINUTE_LIMIT_REACHED | 429 | Minute limit reached, wait the number of seconds indicated by the header: x-minute-reset or change subscription plan.
PeriodLimitReached | PERIOD_LIMIT_REACHED | 429 | Period limit reached, wait the number of seconds indicated by the header: x-period-reset or change subscription plan.
ModelsLimitReached | MODELS_LIMIT_REACHED |429 |You have reached the maximal number of custom models. If you want to create a new one, you have to delete one of your custom models first or change your subscription plan.
InternalError | INTERNAL_ERROR | 500 | Internal Error, we have been notified and will fix the problem as soon as possible. Try again later and do not hesitate to contact us if you need help.

## Upload Data
If you want to build custom models, you will have to upload your dataset. You can do it automatically on a CSV by using the function `classifier.upload_documents`.
```python
client.classifier.upload_csv(model_id, "data.csv", fieldnames=["text", "class_id"], delimiter="\t")
```
It will split the dataset in several parts to avoid exceed the payload size limit.
If you have a more specific dataset format, you can do it by using the functions listed on [the API documentation](https://crowlingo.com/docs).


## Wait for training
The function `client.model.train` is asynchronous, that means it will send you a response before the end of the process. Then if you want to perform an action which need a trained model like for example `client.model.deploy`, you have to wait until the end of the process. The training status can be watched with the function `client.model.get`: `training_status` will contain the status of the training, `training_error` will tell you if an error occurred.

All of this process can be easily managed with the function `client.model.wait_training`:

```python
client.model.train(model_id)
client.model.wait_training(model_id)
client.model.deploy(model_id)
```
 

## Rasa

Crowlingo services can be very useful to create a polyglot chatbot using an existing one. The easiest way is to do it through [Rasa](https://github.com/RasaHQ/rasa).
PyCrowlingo provides packages to easily integrate on Rasa.

### Installation

To install rasa dependencies, simply enter the following command:

```bash
pip install PyCrowlingo[rasa]
```

Follow the [Rasa quick start guide](https://rasa.com/docs/rasa/user-guide/building-assistants/) to build your chatbot.

### Usage

Open the file config.yml and modify the pipeline to integrate Crowlingo NLU components.

Here is an example of a chatbot created with Rasa quick start guide::

```yaml
language: en
pipeline:
  - name: PyCrowlingo.Rasa.EntitiesExtractor
    token: "[TOKEN]"
  - name: PyCrowlingo.Rasa.IntentClassifier
    token: "[TOKEN]"
    model_id: "intent_rasa"
```

Train the model:
```bash
rasa train
```

And now, enjoy your multilingual chatbot:
```bash
rasa shell
>>> Your input -> Bonjour !
<<< Hey! How are you ?
>>> Your input -> Va bene :)
<<< Great! Carry on!
>>> Your input -> Bist du ein Roboter oder ein Mensch?
<<< I am a bot powered by Rasa   
```