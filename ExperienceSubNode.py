__author__ = 'Owner'


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
        return self.workPosition.split('at')[0].rstrip()

    def getJobLocation(self):
        return self.workPosition.split('at')[1].rstrip()