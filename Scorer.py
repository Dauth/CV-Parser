from collections import defaultdict
import json
import MatchBox
import Match
import Facade

class Scorer(object):
    """docstring for Scorer"""
    def __init__(self, db):
        self.db = db

    #calculate and stores score in db
    def calculateScore(self):
        results = defaultdict(list)
        #get all MatchBoxes from DB and put in a list
        matchBoxes = self.db.getMatchBoxes()
        emptyMatchBoxes = set()
        #for all matchBoxes in matchBoxes
        for mb in matchBoxes:
            matches = mb.getMatches()
            #for each match in each matchbox
            for curMatch in matches:
                score = 0
                wordSet = curMatch.getMatchedWords()
                #for each word in each match object
                for curWord in wordSet:
                    score += 1
                results[mb.job].append((curMatch.resume.getName(), score))
            results[mb.job].sort(key=lambda x: x[1], reverse = True)
            emptyBox = MatchBox(mb.job)
            emptyMatchBoxes.add(emptyBox)

        self.db.storeMatchBoxes(emptyMatchBoxes)
        self.db.storeResults(results)
        #insert results to db
        '''
        results will be dictionary, key will be job and value will
        be a list of tuples(resume, score) sorted by descending order of 
        scores
        '''


        
