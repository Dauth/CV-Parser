from Matcher import Matcher
from ResumeProcessor import ResumeProcessor
from FacadeStub import FacadeStub
from ResumeNode import ResumeNode
from JobDescNode import JobDescNode
from ScorerStub import ScorerStub

class ControllerStub(object):

    def __init__(self):
        self.facade = FacadeStub()
        self.matcher = Matcher(self.facade)

    def process(self, resume, job):
        resumeNode = ResumeNode("name", "999", "email@email.com", "0", resume)
        jobNode = JobDescNode(job)
        ResumeProcessor.construct(resumeNode)
        ResumeProcessor.construct(jobNode)
        self.facade.storeJob(jobNode)
        self.facade.storeResume(resumeNode)
        self.matcher.matchAll(1)
        self.matcher.matchAll(2)

    def getResults(self):
        scorer = ScorerStub(self.facade)
        scorer.calculateScore()
        if not self.facade.getMatchBoxes():
            print('empty boxes')



main = ControllerStub()
resumeFile = open('qy/sampleResume.json', 'r')
jobFile = open('qy/sampleJob1.json', 'r')
main.process(resumeFile.read(), jobFile.read())
main.getResults()
