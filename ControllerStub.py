import Matcher
import ResumeProcessor
import FacadeStub
import ResumeNode
import JobDescNode

class ControllerStub(object):

	def __init__(self):
		self.facade = FacadeStub()
		self.matcher = Matcher(facade)

	def process(self, resume, job):
		resumeNode = ResumeNode("name", "999", "email@email.com", "0", resume)
		jobNode = JobDescNode(job)
		ResumeProcessor.construct(resume)
		ResumeProcessor.construct(job)
		self.facade.storeJob(job)
		self.facade.storeResume(resume)
		matcher.matchAll(0)
