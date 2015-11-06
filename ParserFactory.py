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
from LanguageParser import LanguageParser
from FieldLocator import FieldLocator

class ParserFactory(object):
    __parserClassesDict = {"education": EducationParser,
                           "experience": ExperienceParser,
                           "skills": SkillsParser,
                           "language": LanguageParser}

    @staticmethod
    def createParser(nameOfParser, input):
        parserClass = ParserFactory.__parserClassesDict.get(nameOfParser)

        if parserClass:
            return parserClass(input)
        raise NotImplementedError("No such {} parser has been implemented yet".format(nameOfParser))