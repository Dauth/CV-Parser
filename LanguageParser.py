__author__ = 'Owner'
from IParser import IParser
from InformationNode import InformationNode
from ResumeNode import ResumeNode
from JobDescNode import JobDescNode
from FieldsIndexNode import FieldsIndexNode
from nltk import word_tokenize
import re
from DBpediaSpotlight import annotate

class LanguageParser(IParser):
    def __init__(self, input):
        self.content = InformationNode.convertStringIntoList(input)
        self.extractedContent = set()
    def parse(self, node, fieldNode):
        if bool(fieldNode.getLanguageIndex()):
            for start, end in fieldNode.getLanguageIndex().items():
                for line in self.content[start : end]:
                    self.extractedContent.add(line)

            listString = "\n".join(line for line in self.extractedContent)
            if len(self.extractedContent) > 0:
                self.extractedContent = annotate(listString)
                for line in self.extractedContent:
                    if line.get('surfaceForm') not in self.getLanguageKeywordsList() and 'language' in line.get('types').lower():
                        node.addLanguage(line.get('surfaceForm'))
    def getLanguageKeywordsList(self):
        return ['languages']

