__author__ = 'Owner'

class FieldsIndexNode(object):

    def __init__(self):
        self.educationIndex = dict()
        self.skillsIndex = dict()
        self.experienceIndex = dict()

    def addEducationIndex(self, startIndex, endIndex):
        self.educationIndex[startIndex] = endIndex
    def getEducationIndex(self):
        return self.educationIndex
    def isEducationIndexPresent(self):
        return bool(self.educationIndex)

    def addSkillsIndex(self, startIndex, endIndex):
        self.skillsIndex[startIndex] = endIndex
    def getSkillsIndex(self):
        return self.skillsIndex
    def isSkillsIndexPresent(self):
        return bool(self.skillsIndex)

    def addExperienceIndex(self, startIndex, endIndex):
        self.experienceIndex[startIndex] = endIndex
    def getExperienceIndex(self):
        return self.experienceIndex
    def isExperienceIndexPresent(self):
        return bool(self.experienceIndex)