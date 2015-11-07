__author__ = 'Owner'
from InformationNode import InformationNode



class JobDescNode(InformationNode):

    def __init__(self, content, keyword = None):
        super(JobDescNode, self).__init__(content)
        self.setContentTypeAsJob()
        self.importantKeywords = []
        self.addImptKeyword(keyword)


    def addImptKeyword(self, keyword):
        if keyword is not None and isinstance(keyword, str):
                self.importantKeywords += self.convertStringIntoList(keyword)
        elif keyword is not None and isinstance(keyword, list):
                self.importantKeywords += keyword


    def getImptKeywords(self):
        return self.importantKeywords


    def isComputerScience(self):
        return bool(word for word in self.getEducation() if word == 'computer science')