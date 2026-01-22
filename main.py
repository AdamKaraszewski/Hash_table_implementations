from ChainingDictionary import ChainingDictionary
from OpenAddressingDictionary import OpenAddressingDictionary
from ChainingDictionaryWithRehashing import ChainingDictionaryWithRehashing
from OpenAddressingWithRehashingDictionary import OpenAddressingWithRehashingDictionary
import matplotlib.pyplot as plt
import random

chaining_dictionary = ChainingDictionary(10)
chaining_dictionary_rehashing = ChainingDictionaryWithRehashing(10, 20)

open_addressing_dictionary = OpenAddressingDictionary(1000)
open_addressing_dictionary_rehashing = OpenAddressingWithRehashingDictionary(1000, 1, 0.7)

x_axis_chaining_result = []
y_axis_chaining_result = []
while chaining_dictionary.get_elements_number() != 3000:
    first_element = random.randint(0, 1000000000)
    if chaining_dictionary.find(first_element)[0] is None:
        chaining_dictionary.insert(first_element)
        second_element = random.randint(0, 1000000000)
        element, operations = chaining_dictionary.find(second_element)
        x_axis_chaining_result.append(chaining_dictionary.get_elements_number())
        y_axis_chaining_result.append(operations)

x_axis_chaining_rh_result = []
y_axis_chaining_rh_result = []
while chaining_dictionary_rehashing.get_elements_number() != 3000:
    first_element = random.randint(0, 1000000000)
    if chaining_dictionary_rehashing.find(first_element)[0] is None:
        chaining_dictionary_rehashing.insert(first_element)
        second_element = random.randint(0, 1000000000)
        element, operations = chaining_dictionary_rehashing.find(second_element)
        x_axis_chaining_rh_result.append(chaining_dictionary_rehashing.get_elements_number())
        y_axis_chaining_rh_result.append(operations)

x_axis_open_addressing_result = []
y_axis_open_addressing_result = []
while open_addressing_dictionary.get_elements_number() != 1000:
    first_element = random.getrandbits(32)
    if open_addressing_dictionary.find(first_element)[0] is None:
        open_addressing_dictionary.insert(first_element)
        second_element = random.getrandbits(32)
        element, operations = open_addressing_dictionary.find(second_element)
        x_axis_open_addressing_result.append(open_addressing_dictionary.get_elements_number())
        y_axis_open_addressing_result.append(operations)

x_axis_open_addressing_rehashing_result = []
y_axis_open_addressing_rehashing_result = []
while open_addressing_dictionary_rehashing.get_elements_number() != 1000:
    first_element = random.getrandbits(32)
    if open_addressing_dictionary_rehashing.find(first_element)[0] is None:
        open_addressing_dictionary_rehashing.insert(first_element)
        second_element = random.getrandbits(32)
        element, operations = open_addressing_dictionary_rehashing.find(second_element)
        x_axis_open_addressing_rehashing_result.append(open_addressing_dictionary_rehashing.get_elements_number())
        y_axis_open_addressing_rehashing_result.append(operations)

plt.figure()
plt.title("Chain hash table find O(s)")
plt.xlabel('Number of elements in hash table')
plt.ylabel('Number of operations')
plt.grid()
plt.scatter(x_axis_chaining_result, y_axis_chaining_result, label='find O(s)')

plt.figure()
plt.title("Chain hash table with rehashing find O(s)")
plt.xlabel('Number of elements in hash table')
plt.ylabel('Number of operations')
plt.grid()
plt.scatter(x_axis_chaining_rh_result, y_axis_chaining_rh_result, label='find O(s) with rehashing')

plt.figure()
plt.title("Open Addressing find O(s)")
plt.xlabel('Number of elements in hash table')
plt.ylabel('Number of operations')
plt.grid()
plt.scatter(x_axis_open_addressing_result, y_axis_open_addressing_result, label="find 0(s)")

plt.figure()
plt.title("Open addressing with rehashing find O(s)")
plt.xlabel('Number of elements in hash table')
plt.ylabel('Number of operations')
plt.grid()
plt.scatter(x_axis_open_addressing_rehashing_result, y_axis_open_addressing_rehashing_result, label="find 0(s)")

plt.show()
