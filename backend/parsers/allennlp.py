from .base import BaseParser
from typing_extensions import override
from ..commons.parser_input import ParserInputWrapper
from ..commons.parser_output import ParserOutputWrapper


class AllennlpParser(BaseParser):
    @override
    def accept(self, input:ParserInputWrapper) -> ParserOutputWrapper:
        content = input.content
        print(content)

        return ParserOutputWrapper()