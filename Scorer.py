from sets import Set
import json
import MatchBox
import Match
import CustomClassJson

class Scorer(object):
    """docstring for Scorer"""
    def __init__(self, db):
        self.db = db
        self.priorityWords = [None] * 11;

    #calculate and stores score in db
    def calculateScore(self):
        results = dict()
        #get all MatchBoxes from DB and put in a list
        matchBoxes = []

        #for all matchBoxes in matchBoxes
        for mb in matchBoxes:
            matches = mb.getMatches()
            matchList = []
            #for each match in each matchbox
            for curMatch in matches
                score = 0
                wordSet = curMatch.getMatchedWords()
                #for each word in each match object
                for curWord in wordSet:
                    if curWord in piorityWords:
                        score += (11 - priorityWords.index(curWord)) * 2 
                    else:
                        score += 1
                matchList.append((curMatch.resume, score))
            matchList.sort(key=lambda x: x[1]), reverse = True)
            results[mb.job] = matchList;

        resultsJson = json.dumps(results)
        #insert resultsJson to db
        '''
        resultsJson will be dictionary, key will be job and value will
        be a list of tuples(resume, score) sorted by descending order of 
        scores
        '''
    def insertPriority(self, word, priority):
        if priority > 0 and priority <11:
            self.priorityWords[priority] = word

        