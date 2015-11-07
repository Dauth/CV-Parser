__author__ = 'Owner'

class FieldsIndexNode(object):

    def __init__(self):
        self.educationIndex = dict()
        self.skillsIndex = dict()
        self.experienceIndex = dict()
        self.languageIndex = dict()
        self.locationIndex = dict()

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

    def addLanguageIndex(self, startIndex, endIndex):
        self.languageIndex[startIndex] = endIndex
    def getLanguageIndex(self):
        return self.languageIndex
    def isLanguageIndexPresent(self):
        return bool(self.languageIndex)

    def addLocationIndex(self, startIndex, endIndex):
        self.locationIndex[startIndex] = endIndex
    def getLocationIndex(self):
        return self.locationIndex
    def isLocationIndexPresent(self):
        return bool(self.locationIndex)