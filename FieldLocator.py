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
        firstIndex = -1
        self.segmentResume(node, content)
        self.getStartEndLocationResume(node, content)

        # print(node.getContentHeadingIndex())



        # print(self.fieldNode.getExperienceIndex())
        # print(self.fieldNode.getEducationIndex())
        # print(self.fieldNode.getSkillsIndex())
        # for start, end in self.fieldNode.getSkillsIndex().items():
        #     print(start,'---',end)
        # for lineNo, line in enumerate(content):
        #     print('------------------',lineNo)
        #     print(line)


    #Reads the content line by line and check against a list of topic header list. If matches, it will add index of identified headers in the list
    def segmentResume(self, node, content):
        for lineNo, line in enumerate(content):
            wordsInLine = word_tokenize(line)
            if len(wordsInLine) >0 and len(wordsInLine) <= 3:
                for word in wordsInLine:
                    if word in self.getTopicHeaders():
                        node.addToContentHeadingIndex(lineNo)
    def getStartEndLocationResume(self, node, content):
        indexOfLast = len(node.getContentHeadingIndex()) - 1
        for index, item in enumerate(node.getContentHeadingIndex()):
            if(index + 1 <= indexOfLast):
                nextIndex = node.getContentHeadingIndex()[index + 1]
            else:
                nextIndex = len(content) - 1
            wordsList = word_tokenize(content[item])
            for word in wordsList:
                if word in self.getExperienceKeywordList():
                    self.fieldNode.addExperienceIndex(item, nextIndex)
                if word in self.getSkillKeywordList():
                    self.fieldNode.addSkillsIndex(item, nextIndex)
                if word in self.getEducationKeywordsList():
                    self.fieldNode.addEducationIndex(item, nextIndex)
    def getEducationKeywordsList(self):
        return ['education', 'university', 'school', 'polytechnic', 'ite',
                'qualification', 'academic', 'degree', 'phd', 'study']

    def getSkillKeywordList(self):
        return ['skill', 'skills', 'expertise', 'proficiency', 'technical']

    def getExperienceKeywordList(self):
        return ['work', 'experience', 'employment', 'position']

    def getTopicHeaders(self):
        return ["summary", "interests", "experience","projects",
                "languages","skills","expertise",
                "education","publications",
                "achievements",
                "extracurricular activities",
                "publications","patent",
                "referees","responsibilities",
                "certifications","objective",
                "portfolio", "interest", "publication"]

    def getFieldNode(self):
        return self.fieldNode
