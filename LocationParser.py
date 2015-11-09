__author__ = 'Owner'
from IParser import IParser
from InformationNode import InformationNode
from ResumeNode import ResumeNode
from JobDescNode import JobDescNode
from FieldsIndexNode import FieldsIndexNode
from nltk import word_tokenize
import re
from DBpediaSpotlight import annotate
import geocoder
from CountryNode import CountryNode

class LocationParser(IParser):
    def __init__(self, input):
        self.content = InformationNode.convertStringIntoList(input)
        self.extractedContent = set()
    def parse(self, node, fieldNode):
        if bool(fieldNode.getLocationIndex()):
            for start, end in fieldNode.getLocationIndex().items():
                for line in self.content[start : end]:
                    if line:
                        self.extractedContent.add(line)

            listString = "\n".join(line for line in self.extractedContent)
            geo = geocoder.google(listString)
            if geo.json.get('status') == 'OK':
                countryNode = CountryNode(geo.json, geo.country_long.lower(), geo.city.lower())
                node.addLocation(countryNode)

    def getLanguageKeywordsList(self):
        return ['languages']

