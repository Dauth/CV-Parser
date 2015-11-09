__author__ = 'Owner'

class InformationNode(object):

    def __init__(self, contentId, content = None):
        self.contentId = contentId
        self.contentType = None
        self.skillSet = set()
        self.experience = []
        self.education = dict()
        self.content = content or []
        self.language = []
        self.location = None

    #resume or job
    def setContentTypeAsResume(self):
        self.contentType = 'RESUME'

    def setContentTypeAsJob(self):
        self.contentType = 'JOB'

    def getContentType(self):
        return self.contentType

    def getContentId(self):
        return self.contentId

    def setContentId(self, contentId):
        self.contentId = contentId

    def addSkill(self, inputSkill):
        self.skillSet.add(inputSkill)

    def getSkills(self):
        return self.skillSet

    def isSkillsPresent(self):
        return bool(self.skillSet)

    def addExperience(self, inputExperience):
        self.experience.append(inputExperience)

    def getExperience(self):
        return self.experience
    def isExperiencePresent(self):
        return bool(self.experience)


    def addEducation(self, educationLevel, educationLoc = None):
        self.education[educationLevel] = educationLoc

    def getEducation(self):
        return self.education
    def isEducationPresent(self):
        return bool(self.education)

    def getContent(self):
        return self.content

    def addContent(self, content):
        self.content += content

    def getLanguage(self):
        return self.language
    def addLanguage(self, language):
        self.language.append(language)
    def isLanguagePresent(self):
        return bool(self.language)

    def getLocation(self):
        return self.location
    def addLocation(self, location):
        self.location = location
    def isLocationPresent(self):
        return bool(self.location)

    # def __repr__(self):
    #     print("----- SKILLS -----")
    #     print(self.getSkills())
    #     print("----- Education -----")
    #     print(self.getEducation())
    #     print("----- Language -----")
    #     print(self.getLanguage())
    #     print("----- Experience -----")
    #     print(self.getExperience())
    #     for i in self.getExperience():
    #         print(i.workPositionOrExp)
    #         print(i.workDuration)
    #     print("----- Location -----")
    #     print(self.getLocation())
    #     print(self.getLocation().getAddress())
    #     print(self.getLocation().getCountry())
    #     print(self.getLocation().getCity())
    @staticmethod
    def convertStringIntoList(inputText):
        return [line for line in inputText[0].lower().split('\n') if line]