__author__ = 'Owner'
from nltk import word_tokenize
from IParser import IParser
from InformationNode import InformationNode
from ResumeNode import ResumeNode
from JobDescNode import JobDescNode
from FieldsIndexNode import FieldsIndexNode
from ExperienceSubNode import ExperienceSubNode
import re

class ExperienceParser(IParser):
    def __init__(self):
        pass
    def parse(self, node, fieldNode):
        content = InformationNode.convertStringIntoList(node.getContent())
        workDuration = ""
        workPosition = ""
        for index in fieldNode.getExperienceIndex():
            for line in content[index + 1:]:
                wordsInList = word_tokenize(line)
                if len(wordsInList) > 2:#so that we only process everything within the experience header
                    workPositionkReg = self.extractWorkPositionUsingAt(line)
                    if workPositionkReg:
                        workPosition = workPositionkReg.group(0)

                    workDurationReg = self.extractDuration(line)
                    if workDurationReg:
                        workDuration = workDurationReg.group(0)

                    if workPosition and workDuration:
                        experienceSubNode = ExperienceSubNode(workPosition, workDuration)
                        node.addExperience(experienceSubNode)
                        workDuration = ""
                        workPosition = ""



    def extractWorkPositionUsingAt(self, line):
        return re.search(r'([A-Za-z\s*]+) at ([A-Za-z\s*]+)', line)
    def extractDuration(self, line):
        return re.search(r'((january|jan|february|feb|march|mar|april|apr|may|june|jun|july|jul|august|aug|september|sep|october|oct|november|nov|december|dec)\s*\d*\s*(to|-)\s*(january|jan|february|feb|march|mar|april|apr|may|june|jun|july|jul|august|aug|september|sep|october|oct|november|nov|december|dec|present|current|now)\s*\d*\s*)', line)
