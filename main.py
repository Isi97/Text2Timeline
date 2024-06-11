from backend.parsers.allennlp import AllennlpParser
from backend.commons.parser_commons import ParserInput, ParserOutput, ParserSettings
from backend.parsers.base import BaseParser
from backend.commons.output_exports import CSVExporter

from backend.parsers.spacy import SpacyParser



with open("resources/texts/Germany.txt", 'r') as file:
        loaded = file.read()





settings: ParserSettings = ParserSettings()
settings.context_radius = 2




spacy_parser: SpacyParser = SpacyParser()
spacy_parser.settings = settings

spacy_input: ParserInput = ParserInput(loaded)
spacy_input.remove_citation_numbers()
spacy_result = spacy_parser.accept(spacy_input)

print("Spacy Done")

# parser: AllennlpParser = AllennlpParser()
# allen_nlp_result: ParserOutput = parser.accept(ParserInput(loaded))
# parser.settings = settings

print("Allen done")



exporter: CSVExporter = CSVExporter()
# exporter.export("output_allenlp", allen_nlp_result)
exporter.export("output_spacy_v3", spacy_result)

print("Exports Done!")

# TODO remove duplicate events from spacy parser