from abc import ABCMeta, abstractmethod

class IDictionary(metaclass=ABCMeta):
    @abstractmethod
    def insert(self, element):
        """ add element to dictionary """
        pass

    @abstractmethod
    def find(self, key):
        """ get specified element from dictionary, if specified element exist find returns it, else returns None"""
    pass

    @abstractmethod
    def delete(self, key):
        """ delete element from dictionary """
    pass