from Matcher import Matcher
from ResumeProcessor import ResumeProcessor
from FacadeStub import FacadeStub
from ResumeNode import ResumeNode
from JobDescNode import JobDescNode
from ScorerStub import ScorerStub
import json, re
import jsonpickle


def openFile(eFile):
    with open(eFile, encoding='utf-8') as inFile:
        return json.load(inFile)

class ControllerStub(object):

    def __init__(self):
        self.facade = FacadeStub()
        self.matcher = Matcher(self.facade)

    def process(self, resume, job):
        resumeNode = ResumeNode("name", "999", "email@email.com", "0", resume)
        jobNode = JobDescNode("0", job)
        ResumeProcessor.construct(resumeNode)
        ResumeProcessor.construct(jobNode)
        self.facade.storeJob(jobNode)
        self.facade.storeResume(resumeNode)
        self.matcher.matchAll(0)

    def getResults(self):
        scorer = ScorerStub(self.facade)
        scorer.calculateScore()
        if not self.facade.getMatchBoxes():
            print('empty boxes')



main = ControllerStub()
resumeFile = openFile('qy/sampleResume.json')
jobFile = openFile('qy/sampleJob1.json')
main.process(resumeFile, jobFile)
main.getResults()
