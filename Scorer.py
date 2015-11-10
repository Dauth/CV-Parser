from collections import defaultdict
import json
from MatchBox import MatchBox
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
            results[mb.getJob().getContentId()] = list();
            for curMatch in matches:
                score = curMatch.getCount()
                results[mb.getJob().getContentId()].append((curMatch.getResume().getContentId(), score))
            results[mb.getJob().getContentId()].sort(key=lambda x: x[1], reverse = True)
            emptyBox = MatchBox(mb.getJob())
            emptyMatchBoxes.add(emptyBox)

        self.db.storeMatchBoxes(emptyMatchBoxes)
        self.db.storeResults(results)
        #insert results to db
        '''
        results will be dictionary, key will be job and value will
        be a list of tuples(resume, score) sorted by descending order of 
        scores
        '''


        
