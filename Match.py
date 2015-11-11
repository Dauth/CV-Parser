
# 1 to 1 match between a resume and a job
# 1 set of matched words
class Match(object):
    def __init__(self, resume, job, count, matchedKeywords = None):
        self.resume = resume
        self.job = job
        self.count = count
        self.matchedKeywords = matchedKeywords

    def getCount(self):
        return self.count
    def getJob(self):
        return self.job
    def getResume(self):
        return self.resume

    def getMatchedKeyWords(self):
        return self.matchedKeywords

