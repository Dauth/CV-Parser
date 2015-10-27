__author__ = 'Owner'

class InformationNode(object):

    def __init__(self, content = None):
        self.contentType = None
        self.skillSet = set()
        self.experience = []
        self.education = []
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

    def addExperience(self, inputExperience):
        self.experience.append(inputExperience)

    def getExperience(self):
        return self.experience

    def addEducation(self, education):
        self.education.append(education)

    def getEducation(self):
        return self.education

    def getContent(self):
        return self.content

    def addContent(self, content):
        self.content += content

    @staticmethod
    def convertStringIntoList(inputText):
        return inputText[0].lower().split('\n')