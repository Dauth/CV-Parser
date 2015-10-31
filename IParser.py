__author__ = 'Owner'
from abc import ABCMeta, abstractmethod

class IParser(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def parse(self, node, fieldNode):
        pass