__author__ = 'Owner'
import re

class ExperienceSubNode(object):
    def __init__(self, workPosition, workDuration = None):
        self.workPosition = workPosition
        self.workDuration = workDuration

    def getWorkPosition(self):
        return self.workPosition
    def setWorkPosition(self, workPosition):
        self.workPosition = workPosition

    def getWorkDuration(self):
        return self.workDuration
    def setWorkDuration(self, workDuration):
        self.workDuration = workDuration

    def getJobTitle(self):
        # temp = re.search(r'\b([a-z ]+?) at ([a-z ]+)\b(?= \w+ \d+ - |$).*', self.workPosition)
        # print(temp.group(1))
        # print(temp.group(2))
        return re.search(r'\b([a-z ]+?) at ([a-z ]+)\b(?= \w+ \d+ - |$).*', self.workPosition).group(1).strip()
        #return self.workPosition.split(' at ', 1)[0].rstrip()

    def getJobLocation(self):
        return re.search(r'\b([a-z ]+?) at ([a-z ]+)\b(?= \w+ \d+ - |$).*', self.workPosition).group(2).strip()
        #return self.workPosition.split(' at ', 1)[1].rstrip()