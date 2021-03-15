from enum import Enum
from typing import List, Optional, Union, Dict, Any

from pydantic import BaseModel, AnyUrl, EmailStr, Field, constr, validator, PositiveInt
from pydantic.schema import datetime

ID_TYPE = constr(regex=r"^[a-zA-Z0-9_\-: ]*$")
NAME_TYPE = constr(regex=r"^[a-zA-Z0-9_\- ]*$")


class Id(BaseModel):
    id: Optional[ID_TYPE] = None


class Similarity(BaseModel):
    similarity: float


class Position(BaseModel):
    start: int
    end: int


class Properties(BaseModel):
    properties: Optional[Union[List[str], Dict[str, Any]]] = Field({},
                                                                   description="Properties associated to each concept",
                                                                   example=['titles.fr', 'titles.en', 'coordinates',
                                                                            'stock_exchange'])


class Text(BaseModel):
    text: Optional[str] = None


class Mention(Position):
    pass


class Mentions(BaseModel):
    mentions: Optional[List[Mention]] = None


class Label(Text, Mentions):
    pass


class Labels(BaseModel):
    labels: Optional[List[Label]] = None


class Weight(BaseModel):
    weight: Optional[float] = Field(None, description="Importance of the concept in the content",
                                    example="0.8752")


class Concept(Id, Weight, Labels, Properties):
    pass


class CustomMentionRes(Position, Similarity):
    pass


class CustomLabelRes(Text):
    mentions: List[CustomMentionRes]


class CustomConceptRes(Id, Properties):
    labels: List[CustomLabelRes]


class Concepts(BaseModel):
    concepts: Optional[List[Concept]] = None


class ClusterProbability(BaseModel):
    cluster_probability: Optional[float] = None


class CorpusDocument(Id, Text, ClusterProbability, Concepts):
    pass


class CorpusDocuments(BaseModel):
    documents: Optional[List[CorpusDocument]] = None


class Fallback(BaseModel):
    fallback: bool = False


class Word(BaseModel):
    word: str


class Texts(BaseModel):
    texts: List[str] = Field(..., description="List of contents to analyze", example=['I am a text'])


class Lang(BaseModel):
    lang: Optional[ID_TYPE] = Field(None, description="Language of the content", example="fr")


class Document(Lang):
    text: str


class Languages(BaseModel):
    languages: Optional[List[ID_TYPE]]


class Url(BaseModel):
    url: str = Field(..., description="Url of the content to analyze",
                     example="https://www.bbc.com/news/world-australia-50341207")


class Cursor(BaseModel):
    cursor: float = 0.0


class BasicArticle(Url, Cursor):
    title: Optional[str] = None
    source_url: Optional[AnyUrl] = None


class Tokens(BaseModel):
    tokens: List[str]


class TokensList(BaseModel):
    tokens: List[List[str]]


class LangInfo(BaseModel):
    code: str
    date: str


class LangsInfo(BaseModel):
    langs: List[LangInfo]


class Domain(BaseModel):
    domain: str


class BasicArticles(BaseModel):
    articles: List[BasicArticle]


class Combination(BaseModel):
    combination: List[str]


class CombinationSimilarity(Combination, Similarity):
    pass


class Similarities(BaseModel):
    similarities: List[CombinationSimilarity]


class Precision(BaseModel):
    precision: float = Field(0.9, description="Precision of concepts recognition (higher => more noise)",
                             example="0.9", ge=0, le=1)


class Normalizations(BaseModel):
    normalizations: List[str] = Field(["norm"], description="List of normalizations to apply", example=["min", "all"])


class Split(BaseModel):
    split: bool = False


class UserDocument(Id, Text):
    pass


class UserDocuments(BaseModel):
    documents: List[UserDocument]


class ConfidenceLang(BaseModel):
    name: Optional[str] = None
    code: Optional[str] = None
    confidence: Optional[float] = None


class ConfidenceLangs(BaseModel):
    languages_confidence: Optional[List[ConfidenceLang]] = None


class Sentence(Text, ConfidenceLangs, Position):
    pass


class Sentences(BaseModel):
    sentences: List[Sentence]


class Documents(BaseModel):
    documents: List[Document]


class Cluster(Concepts, Documents):
    id: Optional[int] = None


class Clusters(BaseModel):
    clusters: Optional[List[Cluster]] = None


class Corpus(Id, Clusters, Concepts, CorpusDocuments):
    pass


class Summary(BaseModel):
    summary: Optional[str]


class CorpusId(BaseModel):
    corpus_id: ID_TYPE


class OptionalCorpusId(BaseModel):
    corpus_id: ID_TYPE = None


class Inserted(BaseModel):
    inserted: List[str]


class NbConcepts(BaseModel):
    nb_concepts: int = 5


class Article(Id, Url, Cursor):
    source: str = Field(..., description="Domain and suffix of url", example="bbc.com")
    category_url: str
    lang: str
    detected_lang: str
    title: str
    text: str
    top_image: str
    images: List[str]
    movies: List[str]
    authors: List[str]
    summary: str
    publish_date: str


class Email(BaseModel):
    email: EmailStr


class Password(BaseModel):
    password: str


class TemporaryToken(BaseModel):
    tmp_token: str


class TemporaryTokenExpiration(BaseModel):
    tmp_token_expiration: datetime


class OptionalModelId(BaseModel):
    model_id: Optional[ID_TYPE] = None


class ModelId(BaseModel):
    model_id: ID_TYPE


class Name(BaseModel):
    name: NAME_TYPE


class ProdVersion(BaseModel):
    prod_version: bool = False


class Variations(BaseModel):
    variations: Dict[str, str] = {}


class VariationsList(BaseModel):
    variations: List[str] = []


class QuestionId(BaseModel):
    question_id: Optional[ID_TYPE] = None


class AnswerId(BaseModel):
    answer_id: Optional[ID_TYPE] = None


class Question(Id, Variations):
    answer_id: Optional[ID_TYPE] = None


class Answer(Id, Variations):
    pass


class ConceptId(BaseModel):
    concept_id: Optional[ID_TYPE] = None


class LabelId(BaseModel):
    label_id: Optional[ID_TYPE] = None


class Entity(Position):
    ent_type: str
    text: str


class Entities(BaseModel):
    entities: Optional[List[Entity]]


class WordSyntax(Position):
    id: int
    text: str
    pos_tag: str
    lemma: str
    dep: str
    head: int
    feats: Dict[str, Any]


class SentenceSyntax(Position):
    words: List[WordSyntax]


class Match(Text, Position):
    pass


class KeyPhrase(Weight, Text):
    pass


class PhraseMatch(Match):
    similarity: float


class ClassId(BaseModel):
    class_id: ID_TYPE = None


class OldClassId(BaseModel):
    old_class_id: ID_TYPE


class NewClassId(BaseModel):
    new_class_id: ID_TYPE


class DocumentId(BaseModel):
    document_id: ID_TYPE


class ClassDetection(ClassId):
    confidence: float
    additional_features: Dict[str, Any] = {}


class Visualize(BaseModel):
    visualize: bool = False


class Visualization(BaseModel):
    visualization: Optional[str] = None


class CommonsPipeline(BaseModel):
    pipeline: Dict[str, Any]
    commons: Dict[str, Any] = {}


class Description(BaseModel):
    description: Optional[str]


class Marker(BaseModel):
    marker: Optional[ID_TYPE]


class Markers(BaseModel):
    markers: Optional[List[ID_TYPE]]


class Version(BaseModel):
    metrics: Optional[Dict[str, Any]]
    version_id: int


class Public(BaseModel):
    public: Optional[bool]


class Error(BaseModel):
    error_id: str
    msg: str


class Category(str, Enum):
    CLASSIFIER: str = "classifier"
    FAQ: str = "faq"
    CONCEPTS: str = "concepts"
    SEARCH_ENGINE: str = "search_engine"

    @classmethod
    def _missing_(cls, value):
        aliases = {"cpt": cls.CONCEPTS,
                   "clf": cls.CLASSIFIER}
        if value in aliases:
            return aliases[value]
        return super()._missing_(value)


class ModelTypeEnum(str, Enum):
    SVM: str = "svm"
    DEEP: str = "deep"


class OptionalFeatures(BaseModel):
    optional_features: Dict[str, Union[str, int]] = {}


class CustomConcept(Id, Properties, Markers):
    pass


class CustomLabel(Id, ConceptId, Document, Markers):
    precision: float = 0.75


class CustomDocument(Id, Document, ClassId, OptionalFeatures, Markers):
    pass


class CustomQuestion(Variations, Id, AnswerId, Markers):
    pass


class CustomAnswer(Variations, Id, Markers):
    pass


class QuestionsId(BaseModel):
    questions_id: List[ID_TYPE]


class AnswersId(BaseModel):
    answers_id: List[ID_TYPE]


class ConceptsId(BaseModel):
    concepts_id: List[ID_TYPE]


class LabelsId(BaseModel):
    labels_id: List[ID_TYPE]


class DocumentsId(BaseModel):
    documents_id: List[ID_TYPE]


class Pagination(BaseModel):
    page: int = Field(1, ge=1)
    page_size: int = Field(10, ge=1)


class DocumentModel(Id, Document, ClassId, OptionalFeatures, Markers):
    pass


class LabelModel(Document, Id, ConceptId, Markers):
    pass


class ConceptModel(Id, Properties, Markers):
    pass


class QuestionModel(Id, Variations, AnswerId, Markers):
    pass


class AnswerModel(Id, Variations, Markers):
    pass


class Completeness(BaseModel):
    completeness: float = Field(0.2, gt=0, le=1)


class ClfConfigSVM(BaseModel):
    C: List[int] = [1, 2, 5, 10, 20, 100]
    kernels: List[str] = ["linear"]
    max_cross_validation_folds: int = 5
    probability: bool = True
    class_weight: str = "balanced"
    scoring: str = 'f1_weighted'


class ClfConfigDeep(BaseModel):
    hidden_length: List[int] = [1, 2]
    hidden_neurons: List[int] = [32, 64, 128, 256]
    bidirectional: List[bool] = [False, True]
    dropout: List[float] = [0, 0.1, 0.2, 0.4]
    l2_val: List[float] = [0.001, 0.01, 0.1, 0.2, 0.3]
    optimizer: str = 'adam'
    loss: str = 'categorical_crossentropy'
    metrics: List[str] = ['accuracy']
    max_epochs: int = 150
    monitor: str = 'val_loss'
    patience: int = 5


class SplitData(BaseModel):
    train_ratio: float = Field(0.8, le=1.0, gt=0.0)


class ClfConfig(SplitData, ClfConfigSVM, ClfConfigDeep):
    pass


class FaqSearchResult(BaseModel):
    question: Optional[Question]
    answer: Optional[Answer]
    similarity: Optional[float]


class ModelConfig(BaseModel):
    model_config: Optional[ClfConfig]

    @validator("model_config", always=True)
    def set_default_config(cls, v):
        if v:
            return v
        return ClfConfig()


class CollaboratorPermissions(BaseModel):
    query: bool = True
    read: bool = False
    write: bool = False
    deploy: bool = False
    train: bool = False
    collaborators: bool = False


class Permissions(BaseModel):
    permissions: Optional[CollaboratorPermissions]

    @validator("permissions", always=True)
    def set_default_permissions(cls, v):
        if v:
            return v
        return CollaboratorPermissions()


class ModelType(BaseModel):
    model_type: Optional[Union[ModelTypeEnum, str]] = None


class TrainRatio(BaseModel):
    train_ratio: Optional[float] = Field(None, gt=0, le=1, example=0.8)


class MaxTrainingTime(BaseModel):
    max_training_time: Optional[PositiveInt] = Field(None, example=3600)


class HyperParameters(BaseModel):
    hyper_parameters: Optional[Dict[str, Any]] = None


class NbTrainings(BaseModel):
    nb_trainings: Optional[int] = Field(None, ge=1, le=20, example=10)


class Readme(BaseModel):
    readme: Optional[str] = None


class Metadata(BaseModel):
    metadata: Optional[Dict[str, Any]]


class ModelInfo(ModelId, Name, Description, Markers, Public, Readme, Metadata):
    versions: Dict[str, Version]
    category: str
    training_status: str
    training_progress: int
    training_error: Optional[str]
    training_start: Optional[str]
    training_end: Optional[str]
    deploying_start: Optional[str]
    deploying_end: Optional[str]
    owner: str
    collaborators: Dict[str, int]
    deployed: bool


class SearchResult(Text, Weight):
    pass


class LangSearchResult(BaseModel):
    keywords: Dict[str, List[SearchResult]]


class SearchEngineKeyword(Text, Lang):
    pass


class Upsert(BaseModel):
    upsert: bool = False
