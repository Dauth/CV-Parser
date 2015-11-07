class FacadeStub(object):

	def __init__(self):
		self.db = {'jobs': set(), 'resumes': set(), 'matchboxes': set(),
			'new_jobs': set(), 'new_resumes': set()}

	def storeJob(self, job):
		self.db['new_jobs'].union(set([job]))

	def storeResume(self, resume):
		self.db['new_resumes'].union(set([resume]))

	def storeMatchBoxes(self, boxes):
		self.db['matchboxes'] = boxes

	def addMatchBoxes(self, boxes):
                self.db['matchboxes'].union(boxes)

	def getAllJobs(self):
		return self.db['jobs']

	def getAllResumes(self):
		return self.db['resumes']

	def getNewJobs(self):
		new_jobs = self.db['new_jobs']
		self.db['new_jobs'] = set()
		self.db['jobs'].union(new_jobs)
		return new_jobs

	def getNewResumes(self):
		new_resumes = self.db['new_resumes']
		self.db['new_resumes'] = set()
		self.db['resumes'].union(new_resumes)
		return new_resumes

	def getMatchBoxes(self):
		return self.db['matchboxes']
