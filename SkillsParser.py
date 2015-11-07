__author__ = 'Owner'
from nltk import word_tokenize
from IParser import IParser
from InformationNode import InformationNode
from ResumeNode import ResumeNode
from JobDescNode import JobDescNode
from FieldsIndexNode import FieldsIndexNode
import Rake
from DBpediaSpotlight import annotate

class SkillsParser(IParser):
    def __init__(self, input):
        self.content = InformationNode.convertStringIntoList(input)
        self.extractedContent = set()

    def parse(self, node, fieldNode):
        if bool(fieldNode.getSkillsIndex()):
            for start, end in fieldNode.getSkillsIndex().items():
                for line in self.content[start : end]:
                    if line and 'page' not in line:
                        self.extractedContent.add(line)
            listString = "\n".join(line for line in self.extractedContent)
            self.extractedContent = [i.get('surfaceForm') for i in annotate(listString)]
            for line in self.extractedContent:
                if line not in self.getSkillKeywordList():
                    node.addSkill(line)

        # for line in self.extractedContent:
        #     try:
        #         result = annotate(line)
        #         for word in result:
        #             node.addSkill(word)
        #     except:
        #         print('Error in annotating {}'.format(line))
    def getSkillKeywordList(self):
        return ['skill', 'skills', 'expertise', 'proficiency', 'technical', 'qualification', 'qualifications', 'responsibilities']