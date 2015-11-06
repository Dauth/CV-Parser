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
import CustomClassJson


class ResumeProcessor(object):

    __parserList = ["education",
                    "skills",
                    "experience",
                    "language",
                    "location"]

    @staticmethod
    def construct(node):
        fl = FieldLocator()
        fl.identifyFields(node)

        for parserType in ResumeProcessor.__parserList:
            parser = ParserFactory.createParser(parserType, node.getContent())
            parser.parse(node, fl.getFieldNode())
            # print(fl.getFieldNode().getSkillsIndex())
            # print(fl.getFieldNode().getEducationIndex())
            # print(fl.getFieldNode().getExperienceIndex())
            

