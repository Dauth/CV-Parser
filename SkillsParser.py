__author__ = 'Owner'
from nltk import word_tokenize
from IParser import IParser
from InformationNode import InformationNode
from ResumeNode import ResumeNode
from JobDescNode import JobDescNode
from FieldsIndexNode import FieldsIndexNode

class SkillsParser(IParser):
    def __init__(self):
        pass

    def parse(self, node, fieldNode):
        content = InformationNode.convertStringIntoList(node.getContent())
        for line in content[fieldNode.getSkillsIndex() + 1:]:
            if line:
                node.addSkill(line)
            else:
                break

