from backend.parsers.allennlp import AllennlpParser
from backend.commons.parser_commons import ParserInput, ParserOutput, ParserSettings
from backend.parsers.base import BaseParser
from backend.commons.output_exports import CSVExporter

import nltk.data


with open("resources/texts/Germany.txt", 'r') as file:
        loaded = file.read()

tokenizer = nltk.data.load('nltk:tokenizers/punkt/english.pickle')
tokenized = tokenizer.tokenize(loaded) # type: ignore



parser: AllennlpParser = AllennlpParser()
settings: ParserSettings = ParserSettings()
settings.context_radius = 2

parser.settings = settings




result: ParserOutput = parser.accept(ParserInput(tokenized))




print("Number of events: " + str(len(result)))

exporter: CSVExporter = CSVExporter()
exporter.export("output", result)

print("Done!")
