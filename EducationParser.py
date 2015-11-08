__author__ = 'Owner'
from IParser import IParser
from InformationNode import InformationNode
from ResumeNode import ResumeNode
from JobDescNode import JobDescNode
from FieldsIndexNode import FieldsIndexNode
from nltk import word_tokenize
import re
from DBpediaSpotlight import annotate


class EducationParser(IParser):
    def __init__(self, input):
        self.content = InformationNode.convertStringIntoList(input)
        self.extractedContent = set()

    def parse(self, node, fieldNode):
        print(fieldNode.getEducationIndex())
        if bool(fieldNode.getEducationIndex()):
            if(node.getContentType() == 'RESUME'):
                self.extractEducationFromResume(node, fieldNode)
            else:
                self.extractEducationFromJob(node, fieldNode)

    def extractEducationFromJob(self, node, fieldNode):
        for start, end in fieldNode.getEducationIndex().items():
            for line in self.content[start : end]:
                wordsList = word_tokenize(line)
                if len(wordsList) > 0:
                    for word in wordsList:
                        if word in self.getEducationLevel():
                            self.extractedContent.add(line)
        listString = "\n".join(line for line in self.extractedContent)
        try:
            self.extractedContent = [i.get('surfaceForm') for i in annotate(listString)]
            for line in self.extractedContent:
                if line in self.getEducationLevel() and line not in self.getIgnoredKeywords():
                    educationType = line
                if line not in self.getEducationLevel() and line not in self.getIgnoredKeywords():
                    node.addEducation(educationType +" in "+ line, None)
        except:
            pass

    def extractEducationFromResume(self, node, fieldNode):
        educationLevel = ""
        educationLocation = ""
        for start, end in fieldNode.getEducationIndex().items():
            for line in self.content[start : end]:
                wordsList = word_tokenize(line)
                if len(wordsList) > 0:
                    for word in wordsList:
                        if word in self.getEducationLevel():
                            educationLevel = line
                        if word in self.getEducationLocation():
                            educationLocation = line
                        if educationLevel and educationLocation:
                            if educationLevel == educationLocation:
                                node.addEducation(educationLevel)
                            else:
                                node.addEducation(educationLevel, educationLocation)
                            educationLocation= ""
                            educationLevel = ""


    def getIgnoredKeywords(self):
        return ['discipline', 'preferred', 'field']
    def getEducationLevel(self):
        return ['o-level', 'a-level', 'ite', 'nitec', 'master\'s', 'master', 'phd', 'diploma', 'doctor', 'msc', 'bachelor', 'bachelor\'s', 'bachelor degree']

    def getEducationLocation(self):
        return ['university', 'school', 'college', 'polytechnic', 'institute', 'faculty', 'institution']

    def getEducationArea(self):
        return ['computer science', 'information systems']

    def getDuration(self, line):
        return re.search(r'\s*(jan|january|feb|february|mar|march|apr|april|may|jun|june|jul|july|aug|august|sep|september|oct|october|nov|november|dec|december)\s*(\d*)\s*(-|to)?\s*(jan|january|feb|february|mar|march|apr|april|may|jun|june|jul|july|aug|august|sep|september|oct|october|nov|november|dec|december|current|present)\s*(\d)*', line)