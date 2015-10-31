__author__ = 'Owner'

class FieldsIndexNode(object):

    def __init__(self):
        self.educationIndex = -1
        self.skillsIndex = -1
        self.experienceIndex = []

    def setEducationIndex(self, num):
        self.educationIndex = num
    def getEducationIndex(self):
        return self.educationIndex
    def isEducationIndexPresent(self):
        return bool(self.educationIndex)

    def setSkillsIndex(self, num):
        self.skillsIndex = num
    def getSkillsIndex(self):
        return self.skillsIndex
    def isSkillsIndexPresent(self):
        return bool(self.skillsIndex)

    def setExperienceIndex(self, num):
        self.experienceIndex.append(num)
    def getExperienceIndex(self):
        return self.experienceIndex
    def isExperienceIndexPresent(self):
        return bool(self.experienceIndex)