from Match import Match
from MatchBox import MatchBox
from ResumeNode import ResumeNode
from JobDescNode import JobDescNode
from Facade import Facade

class Matcher(object):
    db = None

    def __init__(self, db):
        self.db = db

    def match(self, resume, job):
        s = set()
        #do matching
        #keywords = job.getImptKeywords()
        required_experience = set(job.getExperience())
        required_education = set(job.getEducation())
        required_skills = job.getSkills()
        experience = set(resume.getExperience())
        education = set(resume.getEducation())
        skills = resume.getSkills()
        s.update(required_experience.intersection(experience))
        s.update(required_education.intersection(education))
        s.update(required_skills.intersection(skills))
        new_match = Match(resume, job, s)
        return new_match

    def matchAll(self, mode = 0):

        #Both new resumes and new jobs are uploaded
        if mode == 0:
            resume_list = self.db.getNewResumes()
            job_list = self.db.getNewJobs()
            boxes = set()

            for job in job_list:
                box = MatchBox(job)
                for resume in resume_list:
                    new_match = match(resume, job)
                    box.addMatch(new_match)
                boxes.union(box)
            self.db.addMatchBoxes(boxes)
            
        #Only new resumes are uploaded
        elif mode == 1:
            resume_list = self.db.getNewResumes()
            boxes = self.db.getMatchBoxes()

            for b in boxes:
                box = b
                for resume in resume_list:
                    job = box.getJob()
                    new_match = self.match(resume, job)
                    box.addMatch(new_match)
                boxes.union(box)
            self.db.storeMatchBoxes(boxes)
            
        #Only new jobs are uploaded
        elif mode == 2:
            resume_list = self.db.getAllResumes()
            job_list = self.db.getNewJobs()
            boxes = set()

            for job in job_list:
                box = MatchBox(job)
                for resume in resume_list:
                    new_match = match(resume, job)
                    box.addMatch(new_match)
                boxes.union(box)
            self.db.addMatchBoxes(boxes)

        else:
            return False
