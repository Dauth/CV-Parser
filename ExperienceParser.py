__author__ = 'Owner'
from nltk import word_tokenize
from IParser import IParser
from InformationNode import InformationNode
from ResumeNode import ResumeNode
from JobDescNode import JobDescNode
from FieldsIndexNode import FieldsIndexNode
from ExperienceSubNode import ExperienceSubNode
import re
from DBpediaSpotlight import annotate

class ExperienceParser(IParser):
    def __init__(self, input):
        self.content = InformationNode.convertStringIntoList(input)
        self.extractedContent = set()
    def parse(self, node, fieldNode):
        if bool(fieldNode.getExperienceIndex()):
            if node.getContentType() == 'RESUME':
                self.extractFromResume(node, fieldNode)
                self.extractFromJob(node, fieldNode)
            else:
                self.extractFromJob(node, fieldNode)


    def extractFromJob(self, node, fieldNode):
        for start, end in fieldNode.getExperienceIndex().items():
            for line in self.content[start : end]:
                if 'work experience' == line:#don't process work experience, only process experience
                    break
                wordsInList = word_tokenize(line)
                for word in wordsInList:
                    if word in self.getExperienceKeywordList():# to tackle solely requirements section as there can be a mixture of key requirements and skills section
                        self.extractedContent.add(line)
        for line in self.extractedContent:
            wordsInList = word_tokenize(line)
            try:
                annotatedList = [i.get('surfaceForm') for i in annotate(line)]
                yearIndex = None
                year = 'year'
                years = 'years'
                if years in wordsInList or year in wordsInList:
                    yearIndex = wordsInList.index(years) or wordsInList.index(year)
                for word in annotatedList:
                    if yearIndex is not None:
                        experienceSubNode = ExperienceSubNode(word, " ".join(wordsInList[yearIndex-1 : yearIndex+1]))
                    else:
                        experienceSubNode = ExperienceSubNode(word, None)
                    node.addExperience(experienceSubNode)
            except:
                pass


    def extractFromResume(self, node, fieldNode):
        workDuration = ""
        workPosition = ""
        for start, end in fieldNode.getExperienceIndex().items():
            for line in self.content[start : end]:
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

    def getIgnoredWords(self):
        return ['work', 'experience', 'work experience']

    def getExperienceKeywordList(self):
        return ['work', 'experience', 'employment', 'position', 'proficient', 'year', 'years', 'expertise']