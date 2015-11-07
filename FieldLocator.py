__author__ = 'Owner'
import string
from InformationNode import InformationNode
from ResumeNode import ResumeNode
from JobDescNode import JobDescNode
from FieldsIndexNode import FieldsIndexNode
from nltk import word_tokenize
class FieldLocator(object):

    def __init__(self):
        self.fieldNode = FieldsIndexNode()
        self.contentHeadingIndex = []

    def identifyFields(self, node):
        content = InformationNode.convertStringIntoList(node.getContent())
        firstIndex = -1
        self.segmentResume(node, content)
        self.contentHeadingIndex = sorted(set(self.contentHeadingIndex), key=self.contentHeadingIndex.index)
        self.getStartEndLocationResume(node, content)
        print(self.contentHeadingIndex)
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
            wordsInLine = [word for word in wordsInLine if word not in string.punctuation]
            if len(wordsInLine) >0 and len(wordsInLine) <= 4:
                for word in wordsInLine:
                    if word in self.getTopicHeaders():
                        self.contentHeadingIndex.append(lineNo)
    def getStartEndLocationResume(self, node, content):
        indexOfLast = len(self.contentHeadingIndex) - 1
        for index, item in enumerate(self.contentHeadingIndex):
            if(index + 1 <= indexOfLast):
                nextIndex = self.contentHeadingIndex[index + 1]
            else:
                nextIndex = len(content)
            wordsList = word_tokenize(content[item])
            for word in wordsList:
                if word in self.getExperienceKeywordList():
                    self.fieldNode.addExperienceIndex(item, nextIndex)
                if word in self.getSkillKeywordList():
                    self.fieldNode.addSkillsIndex(item, nextIndex)
                if word in self.getEducationKeywordsList():
                    self.fieldNode.addEducationIndex(item, nextIndex)
                if word in self.getLanguageKeywordsList():
                    self.fieldNode.addLanguageIndex(item, nextIndex)
                if word in self.getLocationKeywordList():
                    self.fieldNode.addLocationIndex(item, nextIndex)

    def getLanguageKeywordsList(self):
        return ['languages']
    def getEducationKeywordsList(self):
        return ['education', 'university', 'school', 'polytechnic', 'ite',
                'academic', 'degree', 'phd', 'study', 'requirements']

    def getSkillKeywordList(self):
        return ['skill', 'skills', 'expertise',
                'proficiency', 'technical', 'qualification',
                'qualifications', 'responsibilities']

    def getExperienceKeywordList(self):
        return ['work', 'experience', 'employment', 'position', 'requirements']

    def getLocationKeywordList(self):
        return ['location']

    def getTopicHeaders(self):
        return ["summary", "interests", "experience","projects",
                "languages","skills","expertise",
                "education","publications", "achievements",
                "extracurricular activities", "publications","patent",
                "referees","responsibilities",
                "certifications", "certification",
                "objective","portfolio",
                "interest", "publication",
                "qualification", "qualifications", "skill",
                'paper', 'papers', 'experiences',
                'activity', 'activities', 'objective', 'history', 'courses', 'course', 'knowledge', 'technical',
                'proficiency', 'proficiencies', 'requirements', 'requirement', 'location', 'description']

    def getFieldNode(self):
        return self.fieldNode
