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

    ###uncomment for resume
    # resume = openFile('D:\install location\pycharm\python\\nltkProj\data\\DesmondLim2.json')
    # print(resume)
    # personA = ResumeNode("desmond", '97859875', 'desmond@gmail.com', '456', resume)

    ###uncomment for job desc
    resume = openFile('D:\install location\pycharm\python\\nltkProj\data\\sampleJob2.json')
    print(resume)
    personA = JobDescNode(resume)


    ResumeProcessor.construct(personA)
    print("----- SKILLS -----")
    print(personA.getSkills())
    print("----- Education -----")
    print(personA.getEducation())
    print("----- Language -----")
    print(personA.getLanguage())
    print("----- Experience -----")
    print(personA.getExperience())
    for i in personA.getExperience():
        print(i.workPosition)
        print(i.workDuration)


    # ## FOR PRINTING OUT THE LINES IN CONTENT
    # for i, j in enumerate(InformationNode.convertStringIntoList(personA.getContent())):
    #     print('------------------------------- ',i)
    #     print(j)
    #
    # temp = CustomClassJson.encodeClassToJson(personA)
    # with open('sampleJob2.json', 'w') as outfile:
    #     json.dump(temp, outfile)








if __name__ == "__main__":
    main()

