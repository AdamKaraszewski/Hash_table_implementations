from ChainingDictionary import ChainingDictionary

class ChainingDictionaryWithRehashing(ChainingDictionary):
    """
    ChainingDictionaryWithRehashing is an implementation of IDictionary which uses chaining method and rehashing.

    constraints:
    - this implementation operates on positive integers,
    - hash function h(element) = element % list_size.
    """

    def __init__(self, size, max_value):
        super().__init__(size)
        self.size = 0
        self.max_value = max_value

    def __new_data(self, new_size):
        new_list = [[] for _ in range(new_size)]
        for tab in self.list:
            for element in tab:
                new_list[element % len(new_list)].append(element)
        return new_list

    def insert(self, element):
        sublist_index, index, comparisons_number = self._find_index(element)
        if index == -1:
            self.list[sublist_index].append(element)
            self.size += 1
            if self.size > len(self.list) * self.max_value:
                self.list = self.__new_data(len(self.list) * 2)
        else:
            self.list[sublist_index][index] = element

    def delete(self, element):
        sublist_index, index, comparisons_number = self._find_index(element)
        if index == -1:
            self.list[sublist_index][index] = self.list[sublist_index][len(self.list[sublist_index])-1]
            self.list[sublist_index].pop()
            self.size -= 1
            if len(self.list) > 1 and 4 * self.size < len(self.list) * self.max_value:
                self.list = self.__new_data(len(self.list) / 2)

    def get_list(self):
        return self.list