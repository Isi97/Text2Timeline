from typing import List, Dict
from ..commons.temporal import TemporalEntity

import re

class ParserSettings(object):
    def __init__(self, context_radius: int = 0):
        self._context_radius = context_radius

    @property
    def context_radius(self):
        return self._context_radius
    
    @context_radius.setter
    def context_radius(self, radius: int):
        self._context_radius = radius


import nltk

class ParserInput():
    tokenizer = nltk.data.load('nltk:tokenizers/punkt/english.pickle')

    def __init__(self, content):
        self._content = content
        self._raw = content

    def tokenize(self):
        self._cotent = tokenizer.tokenize(content) # type: ignore

    def remove_citations(self):
        pass
    
    # removes Wikipedia-style citations that look like this [123]
    def remove_citation_numbers(self):
        self._content = re.sub(r'\[\d+\]', '', self._content)

    def get_content(self):
        # parsers should use this in case some mandatory preprocessing has to be added
        return self._content




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

    def year_map(self) -> Dict[int, List[TemporalEntity]]:
        if self._year_map is not None:
            return self._year_map

        year_map = {}
        for temporal_entity in self.content:
            if temporal_entity.year not in year_map:
                year_map[temporal_entity.year] = []

            year_map[temporal_entity.year].append(temporal_entity)
        
        self._year_map = year_map
        return self._year_map

    def years(self) -> List[int]:
        if self._years is not None:
            return self._years

        year_map = self.year_map()
        years: List[int] = list(year_map.keys())
        years = sorted(years)
        self._years = years

        return self._years