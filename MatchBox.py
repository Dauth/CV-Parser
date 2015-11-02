from sets import Set
import Match

#aggregation of Matches for a job
class MatchBox(object)
    def __init__(self, job):
        self.job = job
        self.matches = set()
    def addMatch(self, new_match):
        self.matches.add(new_match)
    def getMatches(self):
        return self.matches
    def getJob(self):
        return self.job
