from backend.parsers.allennlp import AllennlpParser
from backend.commons.parser_commons import ParserInput, ParserOutput, ParserSettings
from backend.parsers.base import BaseParser
from backend.commons.output_exports import CSVExporter

from backend.parsers.spacy import SpacyParser
import nltk.data


with open("resources/texts/Germany.txt", 'r') as file:
        loaded = file.read()

tokenizer = nltk.data.load('nltk:tokenizers/punkt/english.pickle')
tokenized = tokenizer.tokenize(loaded) # type: ignore




settings: ParserSettings = ParserSettings()
settings.context_radius = 2




spacy_parser: SpacyParser = SpacyParser()
spacy_parser.settings = settings

spacy_result = spacy_parser.accept(ParserInput(loaded))

print("Spacy Done")

# parser: AllennlpParser = AllennlpParser()
# allen_nlp_result: ParserOutput = parser.accept(ParserInput(tokenized))
# parser.settings = settings

print("Allen done")



exporter: CSVExporter = CSVExporter()
# exporter.export("output_allenlp", allen_nlp_result)
exporter.export("output_spacy", spacy_result)

print("Exports Done!")

# TODO remove duplicate events from spacy parser