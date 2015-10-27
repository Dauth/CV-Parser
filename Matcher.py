from sets import Set
import Match
import MatchBox
import ResumeNode
import JobDescNode
import CustomClassJson

class Matcher(object):
    db = None
    count = 0

    def __init__(self, db):
        self.db = db

    def match(self, resume, job):
        s = set()
        #do matching
        keywords = job.getImptKeywords()
        for i in keywords:
            #loop iterating through resume words
            #compare
            
        new_match = Match(resume, job, s)
        return new_match

    def matchAll(self):
        #get all resumes from db
        #get all jobs from db
        
        #loop iterating all jobs
        box = MatchBox(job)
        #loop iterating all resumes
        new_match = match(resume, job)
        box.addMatch(new_match)
        #end loop
        #push box to db
        #end loop
