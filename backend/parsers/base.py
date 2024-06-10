from abc import ABCMeta, abstractmethod
from ..commons.parser_input import ParserInputWrapper
from ..commons.parser_output import ParserOutputWrapper



class BaseParser():
    @abstractmethod
    def accept(self, input: ParserInputWrapper) -> ParserOutputWrapper:
        raise NotImplemented