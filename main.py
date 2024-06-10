from backend.parsers.allennlp import AllennlpParser
from backend.commons.parser_input import ParserInputWrapper

x = AllennlpParser()

x.accept(ParserInputWrapper("basic package setup"))

