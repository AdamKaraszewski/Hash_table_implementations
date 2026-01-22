from IDictionary import IDictionary
from NoFreeSpaceLeftException import NoSpaceLeftException

class OpenAddressingDictionary(IDictionary):
    """
    OpenAddressingDictionary is an implementation of IDictionary which uses open hashing method

    constraints:
    - this implementation operates on positive integers,
    - hash function h(element) = element % list_size and step = 1
    """

    def __init__(self, list_size):
        self.list = [-1] * list_size

    def _empty(self, index):
        return self.list[index] == -1

    def _deleted(self, index):
        return self.list[index] == -2

    def _scan_for(self, element):
        hash_index = element % len(self.list)
        step = 1
        deleted = -1
        index = hash_index
        comparisons_number = 1
        while not self._empty(index):
            comparisons_number += 1
            if self._deleted(index):
                if deleted == -1:
                    deleted = index
            elif self.list[index] == element:
                return index, comparisons_number
            index = (index + step) % len(self.list)
            if index == hash_index:
                return deleted, comparisons_number
        if deleted != -1:
            return deleted, comparisons_number
        return index, comparisons_number

    def find(self, element):
        index, comparisons_number = self._scan_for(element)
        if index == -1 or self._empty(index) or self._deleted(index):
            return None, comparisons_number
        return self.list[index], comparisons_number

    def insert(self, element):
        index, comparisons_number = self._scan_for(element)
        if index == -1:
            raise NoSpaceLeftException("No space left")
        self.list[index] = element
        return comparisons_number

    def delete(self, element):
        index, comparisons_number = self._scan_for(element)
        if index != -1 and not self._empty(index):
            self.list[index] = -2
        return comparisons_number

    def get_elements_number(self):
        elements_number = 0
        for element in self.list:
            if element != -1 and element != -2:
                elements_number += 1
        return elements_number

    def get_list(self):
        return self.list
