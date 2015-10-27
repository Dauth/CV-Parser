__author__ = 'Owner'
from IParser import IParser
from InformationNode import InformationNode
from ResumeNode import ResumeNode
from JobDescNode import JobDescNode
from FieldsIndexNode import FieldsIndexNode
from nltk import word_tokenize
import re

class EducationParser(IParser):
    def __init__(self):
        pass
    def parse(self, node, fieldNode):
        content = InformationNode.convertStringIntoList(node.getContent())
        educationDict = dict()
        educationLevel = ""
        educationLocation = ""
        for line in content[fieldNode.getEducationIndex():]:
            if line:
                test = word_tokenize(line)
                for word in test:
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

            else:#hit empty line
                break
    def getEducationLevel(self):
        return ['o-level', 'a-level', 'ite', 'nitec', 'master\'s', 'master', 'phd', 'diploma', 'doctor', 'msc', 'bachelor']

    def getEducationLocation(self):
        return ['university', 'school', 'college', 'polytechnic', 'institute', 'faculty', 'institution']

    def getDuration(self, line):
        return re.search(r'\s*(jan|january|feb|february|mar|march|apr|april|may|jun|june|jul|july|aug|august|sep|september|oct|october|nov|november|dec|december)\s*(\d*)\s*(-|to)?\s*(jan|january|feb|february|mar|march|apr|april|may|jun|june|jul|july|aug|august|sep|september|oct|october|nov|november|dec|december|current|present)\s*(\d)*', line)