from Match import Match

#aggregation of Matches for a job
class MatchBox(object):
    def __init__(self, job):
        self.job = job
        self.matches = set()
    def addMatch(self, new_match):
        self.matches.add(new_match)
    def getMatches(self):
        return self.matches
    def getJob(self):
        return self.job
<<<<<<< HEAD
    def __iter__(self):
        return MatchBoxIterator(self.matches)
    
class MatchBoxIterator(object):
    def __init__(self, data):
        self.data = data
    def __iter__(self):
        return self
    def __next__(self):
        if not self.data:
            raise StopIteration
        return self.data.pop()
=======
>>>>>>> aa771d1a30131f6bdbae7f6ae89ca278b373b5be
