from abc import ABCMeta, abstractmethod

class IDictionary(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, size):
        """ create object with specified size list """
        pass

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

    @abstractmethod
    def get_elements_number(self):
        """ get all elements number """
    pass

    @abstractmethod
    def get_list(self):
        """ get list """
    pass