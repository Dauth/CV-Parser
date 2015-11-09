__author__ = 'Owner'
from nltk import word_tokenize
import json, re
import jsonpickle
from InformationNode import InformationNode
from ResumeNode import ResumeNode
from JobDescNode import JobDescNode
from FieldsIndexNode import  FieldsIndexNode
from EducationParser import EducationParser
from SkillsParser import SkillsParser
from ExperienceParser import ExperienceParser
from FieldLocator import FieldLocator
from ParserFactory import ParserFactory
from ResumeProcessor import ResumeProcessor
import CustomClassJson
import jellyfish
from Matcher import Matcher
def saveFile(fileLocation, tempList, keyword):
    fileName = ''.join((fileLocation, keyword, '.json'))
    with open(fileName, 'w') as outfile:
        json.dump(tempList, outfile, indent=1, ensure_ascii=False)
    print('saved')

def openFile(eFile):
    with open(eFile, encoding='utf-8') as inFile:
        return json.load(inFile)

def test(node):
    node.setName('john')
def main():

    # ###uncomment for resume
    resume = openFile('D:\install location\pycharm\python\\nltkProj\data\\input\\resume3.json')
    print(resume)
    resumeNode = ResumeNode("desmond", '97859875', 'desmond@gmail.com', '456', resume)

    ##uncomment for job desc
    content = openFile('D:\install location\pycharm\python\\nltkProj\data\\input\\jobdesc3.json')
    keywords = openFile('D:\install location\pycharm\python\\nltkProj\data\\keywords.json')
    # print(resume)
    #
    jobNode = JobDescNode("545646", content, keywords)
    # print(personA.getImptKeywords())

    ResumeProcessor.construct(jobNode)
    ResumeProcessor.construct(resumeNode)

    imptKeywordSet = set(InformationNode.convertStringIntoList(keywords))
    print(imptKeywordSet)
    rskillSet = set(resumeNode.getSkills())
    jskillSet = set(jobNode.getSkills())
    resultSkillSet = rskillSet.intersection(jskillSet)
    resultSkillSet2 = rskillSet.intersection(imptKeywordSet)
    print(rskillSet)
    print(jskillSet)
    print(len(resultSkillSet) + len(resultSkillSet2))
    rLangSet = set(resumeNode.getLanguage())
    jLangSet = set(jobNode.getLanguage())
    resultLangSet = rLangSet.intersection(jLangSet)
    resultLangSet2 = rskillSet.intersection(imptKeywordSet)
    print(rLangSet)
    print(jLangSet)
    print(len(resultLangSet) + len(resultLangSet2))
    rLocationSet = resumeNode.getLocation().getCountry()
    jLocationSet = jobNode.getLocation().getCountry()
    resultLocationSet = int(rLocationSet == jLocationSet)
    print(resultLocationSet)
    print(rLocationSet)
    print(jLocationSet)

    print(resumeNode.getEducation())
    print(jobNode.getEducation())
    print(compareEducationBetweenJobandResume(resumeNode.getEducation(), jobNode.getEducation()))
    print(compareExperienceBetweenJobandResume(resumeNode.getExperience(), jobNode.getExperience(),InformationNode.convertStringIntoList(keywords) ))


def compareEducationBetweenJobandResume(resumeEdu, jobEdu):
    for key in jobEdu:
        eduType = key.split('in')[0].strip()
        eduArea = key.split('in')[1].strip()
        for keyN in resumeEdu:
            if eduArea in keyN and eduType in keyN:
                return 1
    return 0

def compareExperienceBetweenJobandResume(resumeExp, jobExp, imptkeywords):
    resumeSet =set(i.getWorkPositionOrExp() for i in resumeExp)
    jobSet =set(i.getWorkPositionOrExp() for i in jobExp)
    print(resumeSet)
    print(jobSet)
    imptkeywordsSet = set(imptkeywords)
    return len(resumeSet.intersection(jobSet)) + len(resumeSet.intersection(imptkeywordsSet))

if __name__ == "__main__":
    main()

