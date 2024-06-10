from typing import List
from ..commons.temporal import TemporalEntity

class ParserSettings(object):
    def __init__(self, context_radius: int = 0):
        self._context_radius = context_radius

    @property
    def context_radius(self):
        return self._context_radius
    
    @context_radius.setter
    def context_radius(self, radius: int):
        self._context_radius = radius



class ParserInput():
    def __init__(self, content):
        self.content = content



class ParserOutput(object):

    def __init__(self, content: List[TemporalEntity]):
        self._content = content

    @property
    def content(self) -> List[TemporalEntity]:
        return self._content

    @content.setter
    def content(self, content: List[TemporalEntity]):
        self._content = content

    def __len__(self):
        return len(self.content)

    def __str__(self):
        result: str = ""

        for temporal_entity in self.content:
            result += str(temporal_entity) + "\n"

        return result