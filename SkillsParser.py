__author__ = 'Owner'
from nltk import word_tokenize
from IParser import IParser
from InformationNode import InformationNode
from ResumeNode import ResumeNode
from JobDescNode import JobDescNode
from FieldsIndexNode import FieldsIndexNode
import Rake

class SkillsParser(IParser):
    def __init__(self, input):
        self.content = InformationNode.convertStringIntoList(input)
        self.extractedContent = []

    def parse(self, node, fieldNode):
        for start, end in fieldNode.getSkillsIndex().items():
            for line in self.content[start : end - 1]:
                if line and 'page' not in line:
                    self.extractedContent.append(line)
        rake_object = Rake.Rake("nltkstopwords.txt", 1,4,1)

        keywordsList = rake_object.run('\n'.join(self.extractedContent))

        for keyword in keywordsList:
            node.addSkill(keyword[0])