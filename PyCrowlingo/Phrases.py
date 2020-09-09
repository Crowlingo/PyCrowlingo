from .Connector import Connector

from .ApiModels import Phrases as Models


class Phrases(Connector):

    def extract_keys(self, text, lang=None, limit=None, normalize=None):
        return Models.ExtractKeys.fill(**locals()).call(self.client)

    def match(self, text, phrase, lang=None, phrase_lang=None, precision=None, visualize=False):
        return Models.Match.fill(**locals()).call(self.client)

    def rule_based_match(self, text, patterns, lang=None, parameters=None, visualize=None):
        return Models.RuleBasedMatch.fill(**locals()).call(self.client)
