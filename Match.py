
# 1 to 1 match between a resume and a job
# 1 set of matched words
class Match(object):
    def __init__(self, resume, job, word_set):
        self.resume = resume
        self.job = job
        self.word_set = word_set

    def getMatchedWords(self):
        return self.word_set
    def getJob(self):
        return self.job
    def getResume(self):
        return self.resume
