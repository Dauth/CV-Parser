class FacadeStub(object):

	def __init__(self):
		self.db = {'jobs': set(), 'resumes': set(), 'matchboxes': set(),
			'new_jobs': set(), 'new_resumes': set()}

	def storeJob(self, job):
		self.db['new_jobs'].add(job)

	def storeResume(self, resume):
		self.db['new_resumes'].add(resume)

	def storeMatchBoxes(self, boxes):
		self.db['matchboxes'] = boxes

	def addMatchBoxes(self, boxes):
                self.db['matchboxes'].update(boxes)

	def getAllJobs(self):
		return self.db['jobs']

	def getAllResumes(self):
		return self.db['resumes']

	def getNewJobs(self):
		new_jobs = self.db['new_jobs']
		self.db['jobs'].update(new_jobs)
		self.db['new_jobs'] = set()
		return new_jobs

	def getNewResumes(self):
		new_resumes = self.db['new_resumes']
		self.db['resumes'].update(new_resumes)
		self.db['new_resumes'] = set()
		return new_resumes

	def getMatchBoxes(self):
		return self.db['matchboxes']
