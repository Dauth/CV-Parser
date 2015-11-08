__author__ = 'Owner'
from InformationNode import InformationNode



class JobDescNode(InformationNode):

    def __init__(self, contentId, content, keyword = None):
        super(JobDescNode, self).__init__(contentId, content)
        self.setContentTypeAsJob()
        self.importantKeywords = self.addImptKeyword(keyword)



    def addImptKeyword(self, keyword):
        return self.convertStringIntoList(keyword)



    def getImptKeywords(self):
        return self.importantKeywords


    def isComputerScience(self):
        return bool(word for word in self.getEducation() if word == 'computer science')