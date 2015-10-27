__author__ = 'Owner'
from InformationNode import InformationNode
from ResumeNode import ResumeNode
from JobDescNode import JobDescNode
from FieldsIndexNode import FieldsIndexNode
from nltk import word_tokenize
class FieldLocator(object):
    def __init__(self):
        self.fieldNode = FieldsIndexNode()

    def identifyFields(self, node):
        content = InformationNode.convertStringIntoList(node.getContent())
        for lineNo, line in enumerate(content):
            wordsInLine = word_tokenize(line)
            # print("lineeeeeeeeeeeeeeeeeeeeeeeeeeeeee {}".format(lineNo))
            # print(line)
            # print("length  {}".format(len(line)))
            #print(wordsInLine)
            if len(wordsInLine) <= 3:
                self.isKeywordPresentInField(lineNo, wordsInLine)

    def isKeywordPresentInField(self, lineNo, wordsInLine):
        for word in wordsInLine:
            #print(word)
            if word in self.getEducationKeywordsList():
                self.fieldNode.setEducationIndex(lineNo)
            if word in self.getSkillKeywordList():
                self.fieldNode.setSkillsIndex(lineNo)
            if word in self.getExperienceKeywordList():
                self.fieldNode.setExperienceIndex(lineNo)



    def getEducationKeywordsList(self):
        return ['education', 'university', 'school', 'polytechnic', 'ite',
                'qualification', 'academic', 'degree', 'phd', 'study']

    def getSkillKeywordList(self):
        return ['skill', 'skills', 'expertise', 'proficiency', 'technical']

    def getExperienceKeywordList(self):
        return ['work', 'experience', 'employment', 'position']

    def getFieldNode(self):
        return self.fieldNode