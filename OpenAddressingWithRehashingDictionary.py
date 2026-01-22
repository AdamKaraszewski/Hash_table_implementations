from OpenAddressingDictionary import OpenAddressingDictionary

class OpenAddressingWithRehashingDictionary(OpenAddressingDictionary):
    """
    OpenAddressingWithRehashingDictionary is an implementation of IDictionary which uses open hashing method

    constraints:
    - this implementation operates on positive integers
    - hash function h(element) = element % list_size and step = 1
    """
    def __init__(self, size, d, n):
        super().__init__(size)
        self.size = 0
        self.d = d
        self.n = n

    def __new_data(self, new_size):
        new_list = [-1] * new_size
        for src_i in range(len(self.list)):
            if not self._empty(src_i) and not self._deleted(src_i):
                e = self.list[src_i]
                i = self.list[src_i] % len(new_list)
                s = 1
                while new_list[i] != -1:
                    i = (i + s) % len(new_list)
                new_list[i] = self.list[src_i]
        return new_list

    def insert(self, element):
        i = self._scan_for(element)[0]
        if self._empty(i) or self._deleted(i):
            self.list[i] = element
            self.size += 1
            if self.size * self.d > len(self.list) * self.n:
                self.list = self.__new_data(2 * len(self.list))
        else:
            self.list[i] = element

    def delete(self, element):
        i = self._scan_for(element)[0]
        if not self._empty(i) and not self._deleted(i):
            self.list[i] = -2
            self.size -= 1
            if len(self.list) > 1 and self.size * self.d * 4 < len(self.list) * self.n:
                self.list = self.__new_data(len(self.list) / 2)
