from math import log

from backend.commons.parser_commons import ParserInput, ParserOutput
from ..commons.t2t_logging import log_info

from ..parsers.allennlp import AllennlpParser
from ..parsers.flairparser import FlairParser
from ..parsers.spacy import SpacyParser

import threading

class ParserService:
    _default_parsers = []
    _customer_parsers = []

    _threads = []

    def __init__(self) -> None:
        pass

    def init_parsers_async(self) -> None:
        for threadNumber, parser in enumerate(self._default_parsers):
            thread = threading.Thread(target=self.initialize_parser, args=(parser,))
            thread.start()
            self._threads.append(thread)

        for thread in self._threads:
            thread.join()

        log_info("Default parsers finished loading")

    def initialize_parser(self, parser) -> None:
        parser.initialize()

    def load_default_parsers(self) -> None:
        parser1 = AllennlpParser()
        parser2 = FlairParser()
        parser3 = SpacyParser()

        self._default_parsers.append(parser2)
        self._default_parsers.append(parser1)
        self._default_parsers.append(parser3)

    def get_parsers(self) -> list[str]:
        return list(map(lambda x: x._PARSER_NAME, self._default_parsers))


    def confirm_parsers_loaded(self):
        outputs: list[ParserOutput] = []
        for parser in self._default_parsers:
            outputs.append(parser.accept(ParserInput("The quick brown fox jumped over the lazy brown dog in 1999. Seven seas blow seven windows in text to speech.")))

        for o in outputs:
            print(o)



