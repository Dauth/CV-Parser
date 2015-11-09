from collections import defaultdict
from Scorer import Scorer
from Match import Match
from MatchBox import MatchBox
from InformationNode import InformationNode
from ResumeNode import ResumeNode
from JobDescNode import JobDescNode
import json

def saveFile(fileLocation, tempList, keyword):
    fileName = ''.join((fileLocation, keyword, '.json'))
    with open(fileName, 'w') as outfile:
        json.dump(tempList, outfile, indent=1, ensure_ascii=False)
    print('saved')

def openFile(eFile):
    with open(eFile, encoding='utf-8') as inFile:
        return json.load(inFile)

def main():
    resume = openFile('data/DesmondLim2.json')
    print(resume)
    resumeNode = ResumeNode("desmond", '97859875', 'desmond@gmail.com', '456', resume)

    ##uncomment for job desc
    content = openFile('data/sampleJob2.json')
    print(content)
    print('1')
    keywords = openFile('data/keywords.json')
    # print(resume)
    #
    jobNode = JobDescNode("545646", content, keywords)

    arbitrary_number= 666

    match = Match(resumeNode, jobNode, arbitrary_number)
    box = MatchBox(jobNode)
    box.addMatch(match);
    boxes = set();
    boxes.add(box);
    calculateScore(boxes)

def calculateScore(matchBoxes):
    results = defaultdict(list)
    
    for mb in matchBoxes:
        matches = mb.getMatches()
        #for each match in each matchbox
        results[mb.getJob().getContentId()] = list();
        for curMatch in matches:
            score = curMatch.getMatchedWords()
            results[mb.getJob().getContentId()].append((curMatch.getResume().getContentId(), score))
        results[mb.getJob().getContentId()].sort(key=lambda x: x[1], reverse = True)

    print(json.dumps(results))
 
if __name__=="__main__":
    main()



