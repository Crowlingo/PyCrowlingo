from typing import List, Optional, Union, Dict, Any

from pydantic import BaseModel, AnyUrl, EmailStr, Field
from pydantic.schema import datetime


class Id(BaseModel):
    id: Optional[str] = None


class Position(BaseModel):
    start: int
    end: int


class Properties(BaseModel):
    properties: Optional[Union[List[str], Dict[str, Any]]] = Field(None,
                                                                   description="Properties associated to each concept",
                                                                   example=['titles.fr', 'titles.en', 'coordinates',
                                                                            'stock_exchange'])


class ConceptsProperties(BaseModel):
    concepts_properties: Optional[Union[List[str], Dict[str, Any]]] = None


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
    lang: Optional[str] = Field(None, description="Language of the content", example="fr")


class Document(Lang):
    text: str


class Langs(BaseModel):
    langs: List[str]


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


class Similarity(BaseModel):
    similarity: float


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
    corpus_id: str


class OptionalCorpusId(BaseModel):
    corpus_id: str = None


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


class CustomLabel(Text, Lang):
    dest: str


class Annotation(Position):
    label: str


class TrainingDocument(Lang):
    text: str
    annotations: List[Annotation]


class Email(BaseModel):
    email: EmailStr


class Password(BaseModel):
    password: str


class TemporaryToken(BaseModel):
    tmp_token: str


class TemporaryTokenExpiration(BaseModel):
    tmp_token_expiration: datetime


class ModelId(BaseModel):
    model_id: Optional[str] = None


class Variations(BaseModel):
    variations: Dict[str, str] = {}


class QuestionId(BaseModel):
    question_id: Optional[str] = None


class AnswerId(BaseModel):
    answer_id: Optional[str] = None


class Question(Id, Variations):
    answer_id: Optional[str] = None


class Answer(Id, Variations):
    pass


class ConceptId(BaseModel):
    concept_id: Optional[str] = None


class LabelId(BaseModel):
    label_id: Optional[str] = None


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
    class_id: str


class SentenceId(BaseModel):
    sentence_id: str


class ClassDetection(ClassId):
    confidence: float


class Visualize(BaseModel):
    visualize: bool = False


class Visualization(BaseModel):
    visualization: Optional[str] = None


class CommonsPipeline(BaseModel):
    pipeline: Dict[str, Any]
    commons: Dict[str, Any] = {}
