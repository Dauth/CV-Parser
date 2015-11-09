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

    def process(self, resume, job, keyword):
        resumeNode = ResumeNode("name", "999", "email@email.com", "0", resume)
        jobNode = JobDescNode("0", job, keyword)
        ResumeProcessor.construct(resumeNode)
        ResumeProcessor.construct(jobNode)
        self.facade.storeJob(jobNode)
        self.facade.storeResume(resumeNode)
        self.matcher.matchAll(0)

    def getResults(self):
        scorer = ScorerStub(self.facade)
        scorer.calculateScore()

main = ControllerStub()
resumeFile = openFile('qy\\sampleResume.json')
jobFile = openFile('qy\\sampleJob2.json')
keywordFile = openFile('data\\keywords.json')
main.process(resumeFile, jobFile, keywordFile)
main.getResults()
