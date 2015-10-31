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

class ParserFactory(object):
    __parserClassesDict = {"education": EducationParser,
                    "experience": ExperienceParser,
                   "skills": SkillsParser}

    @staticmethod
    def createParser(nameOfParser):
        parserClass = ParserFactory.__parserClassesDict.get(nameOfParser)

        if parserClass:
            return parserClass()
        raise NotImplementedError("No such {} parser has been implemented yet".format(nameOfParser))