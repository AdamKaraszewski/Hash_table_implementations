from IDictionary import IDictionary

class ChainingDictionary(IDictionary):
    """
    ChainingDictionary is an implementation of IDictionary which uses chaining method.

    constraints:
    - this implementation operates on positive integers,
    - hash function h(element) = element % list_size.
    """
    def __init__(self, size):
        self.list = [[] for _ in range(size)]

    def _find_index(self, element):
        """ the function returns the index of the list where element is stored and index of element in returned list """
        comparisons_number = 1 # first operation is calculating sublist index
        list_index = element % len(self.list)
        for i in range(len(self.list[list_index])):
            comparisons_number += 1
            if self.list[list_index][i] == element:
                return list_index, i, comparisons_number
        return list_index, -1, comparisons_number

    def insert(self, element):
        list_index, index, comparisons_number = self._find_index(element)
        if index == -1:
            self.list[list_index].append(element)
        else:
            self.list[list_index][index] = element
        return comparisons_number

    def find(self, element):
        list_index, element_index, comparisons_number = self._find_index(element)
        if element_index == -1:
            return None, comparisons_number
        return self.list[list_index][element_index], comparisons_number

    def delete(self, element):
        list_index, index, comparisons_number = self._find_index(element)
        if index != -1:
            self.list[list_index][index] = self.list[list_index][len(self.list[list_index])-1]
            self.list[list_index].pop()
        return comparisons_number

    def get_elements_number(self):
        elements_number = 0
        for sublist in self.list:
            elements_number += len(sublist)
        return elements_number

    def get_list(self):
        return self.list
