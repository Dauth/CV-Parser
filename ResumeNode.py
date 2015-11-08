__author__ = 'Owner'
from InformationNode import InformationNode

class ResumeNode(InformationNode):

    def __init__(self, name, hpNumber, email, contentId, content = None):
        super(ResumeNode, self).__init__(contentId, content)
        self.education = dict()#overide initial education to dict
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

    def addEducation(self, educationLevel, educationLoc = None):#overide
        self.education[educationLevel] = educationLoc

    def getEducation(self):#overide
        return self.education

    def isBachelorDegree(self):
        return bool(k for k, v in self.education.items() if 'bachelor' in k)

    def isMastersDegree(self):
        return bool(k for k, v in self.education.items() if 'master\s' or 'masters' in k)

    def isPHD(self):
        return bool(k for k, v in self.education.items() if 'phd' in k)

    def isAlevel(self):
        return bool(k for k, v in self.education.items() if 'a-level' in k)

    def isOlevel(self):
        return bool(k for k, v in self.education.items() if 'o-levl' in k)

    def isDiploma(self):
        return bool(k for k, v in self.education.items() if 'diploma' in k)

    def isAreaInDegreePresent(self, area):
        return bool([i for i in self.education if area in i])
