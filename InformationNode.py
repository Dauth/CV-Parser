__author__ = 'Owner'

class InformationNode(object):

    def __init__(self, content = None):
        self.contentType = None
        self.skillSet = set()
        self.qualitySet = set()
        self.educationLevelSet = set()
        self.content = content or []


    #resume or job
    def setContentTypeAsResume(self):
        self.contentType = 'RESUME'

    def setContentTypeAsJob(self):
        self.contentType = 'JOB'

    def getContentType(self):
        return self.contentType

    def addSkill(self, inputSkill):
        self.skillSet.add(inputSkill)

    def getSkills(self):
        return self.skillSet

    def addQualification(self, inputQualification):
        self.qualitySet.add(inputQualification)

    def getQualifications(self):
        return self.qualitySet

    def addEducation(self, education):
        self.educationLevelSet.add(education)

    def getEducation(self):
        return self.educationLevelSet

    def getContent(self):
        return self.content

    def addContent(self, content):
        self.content += content

    @staticmethod
    def convertStringIntoList(inputText):
        return inputText[0].split('\n').lower()