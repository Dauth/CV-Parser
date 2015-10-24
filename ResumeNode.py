__author__ = 'Owner'
from InformationNode import InformationNode

class ResumeNode(InformationNode):

    def __init__(self, name, hpNumber, email):
        super().__init__()
        self.name = name
        self.hpNumber = hpNumber
        self.email = email
        self.setContentTypeAsResume()

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setHpNumber(self, hpNumber):
        self.hpNumber = hpNumber

    def getHpNumber(self):
        return self.hpNumber

    def setEmail(self, email):
        self.email = email

    def getEmail(self):
        return  self.email

    def isBachelorDegree(self):
        return bool([i for i in self.educationLevelSet if 'bachelor' in i])

    def isMastersDegree(self):
        return bool([i for i in self.educationLevelSet if 'master\'s' or 'masters' in i])

    def isPHD(self):
        return bool([i for i in self.educationLevelSet if 'phd' in i])

    def isAlevel(self):
        return bool([i for i in self.educationLevelSet if 'a-level' in i])

    def isOlevel(self):
        return bool([i for i in self.educationLevelSet if 'o-level' in i])

    def isDiploma(self):
        return bool([i for i in self.educationLevelSet if 'diploma' in i])

    def isAreaInDegreePresent(self, area):
        return bool([i for i in self.educationLevelSet if area in i])