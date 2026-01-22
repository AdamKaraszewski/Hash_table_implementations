## What is a hash table?
A hash table is a data structure that provides a set of the following methods:
- insert (element) - insert an element to the table,
- find (element) - get an element from the table,
- delete (element) - delete an element from the table.

**Hash tables presented in this project detect duplicated values - duplicates won't be added to hash table (hash set):**

```python
chaining_dictionary = ChainingDictionary(10) # create an empty hash table 
chaining_dictionary.insert(2) # insert 2 to the hash table <- success
chaining_dictionary.insert(2) # insert 2 to the hash table <- this element won't be inserted, because 2 is just stored
```
## Hash table (set) implementations
This project shows two implementation techniques :
- chain method
- open addressing method


## Chain hash table
A hash table that is based on chain technique uses 2D array

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| - | - | - | - | - | - | - | - | - | - |
|   |   |   |   |   |   |   |   |   |   |

### Chain hash table - insert

Implemented chain hash table calculates the key for specified element using following formula: element % len(self.array) 
 
- insert(element = 2): <br/>
1. calculate key: key = 2 % 10 # <- 2, 
2. check if element = 2 is stored inside subarray (array[key]) O(subarray_size),
3. if subarray doesn't contain element = 2 add it at the end of array.

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| - | - |---| - | - | - | - | - | - | - |
|   |   | 2 |   |   |   |   |   |   |   |

- insert(5): key = 5 % 10 # <- 5

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| - | - |---| - | - |---| - | - | - | - |
|   |   | 2 |   |   | 5 |   |   |   |   |

- insert(22): key = 22 % 10 # <- 2

| 0 | 1 | 2        | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| - | - |----------| - | - |---| - | - | - | - |
|   |   | 2<br/>22 |   |   | 5 |   |   |   |   |

### Chain hash table - find

- find(element = 5) <br/>
1. calculate key: key = 5 % 10 # <- 5
2. check if element = 5 is stored inside array[key = 5] subarray max O(len(array[key = 5]))
3. if element = 5 is present return it, if subarray doesn't contain element = 5 it returns None 

### Chain hash table - delete

- delete(element = 2) <br/>
1. calculate key: key = 2 % 10 # <- 2
2. check if element = 2 is stored inside array[key = 2] subarray. max O(len(array[key = 2]))
3. if element = 2 is present in subarray save its value in result variable result = array[2][i = 0]
4. change array[key = 2][i = 0] = array[key = 2][len(array[2]) - 1] # array[2][0] = array[2][1]

| 0 | 1 | 2                    | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| - | - |----------------------| - | - |---| - | - | - | - |
|   |   | 22<br/><del>22</del> |   |   | 5 |   |   |   |   |
5. remove array[key = 2][i = 0] last element

| 0 | 1 | 2  | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| - | - |----| - | - |---| - | - | - | - |
|   |   | 22 |   |   | 5 |   |   |   |   |

### Chain hash table - time complexity

- insert, O(1 + subarray_size <- when hash set is implemented):
1. calculate key - one operation 
2. add element at the end of subarray - one operation 

- find, optimistic O(1 + 1) and pessimistic O(1 + subarray_size): 
1. calculate key - one operation
2. iterate table until element = array[key][i] - min: one operation - element has index = 0, max: len(array[key]) - element is not stored or element is placed at the last position of subarray 

- delete, optimistic O(1 + 1) and pessimistic O(1 + subarray_size):
1. calculate key - one operation
2. iterate table until element = array[key][i] - min: one operation - element has index = 0, max: 

**If array size is big enough, hashing formula will place elements across all subarrays with equal probability. 
In this case each subarray size is equal S/N, S - all elements stored in hash table, N - subarrays number.** <br/>
Bases on this fact time complexities of hash table (set) methods are:
- find O(1 + s/n)
- insert O(1 + s/n)
- delete O(1 + s/n)

Figure 1. find operation time complexity O(s/n), n = 10, h(element) = element % 10

### Chain hash table - time complexity reduction

Let's find some complexities for find operation:

| 0                            | 1                         | 2  | 3                            | 4                 |
|------------------------------|---------------------------|----|------------------------------|-------------------|
| 15 <br/> 70 <br/> 35<br/> 50 | 1 <br/> 26 <br/> 66 <br/> | 47 | 13 <br/> 8 <br/> 38 <br/> 23 | 64 <br/> 69 <br/> |

find(15), find(1), find(47), find(13), find(64) have O(1 + 1) = **O(2) - min time complexity**<br/>
find(70), find(26), find(8), find(69) have O(1 + 2) = O(3) <br/>
find(35), find(66), find(38) has O(1 + 3) = O(4) <br/>
find(50), find(23) has O(1 + 4) = **O(5) - max time complexity** <br/>

Avg find time complexity: (2 * 5 + 3 * 4 + 4 * 3 + 5 * 2) / 14 = (10 + 12 + 12 + 10) / 14 = 44 / 14 ~= 3,14 
Let's expand array from n = 5 to n = 10. Array expanding time complexity O(s).

| 0 | 1 | 2 | 3           | 4 | 5 | 6           | 7 | 8          | 9 |
| - | - | - |-------------| - | - |-------------| - |------------| - |
| 70 <br/> 50 | 1 | | 13 <br/> 23 | 64 | 15 <br/> 35 <br/> | 66 <br/> 26 | 47 | 8 <br/> 38 | 69 |

find(70), find(1), find(13), find(64), find(15), find(66), find(47), find(8), find(69) have O(1+1) = **O(2) - min time complexity**<br/>
find(50), find(23), find(35), find(26), find(38) have O(1 + 2) = **O(3) - min time complexity**

Avg find time complexity: (2 * 9 + 3 * 5) / 14 = (18 + 15) / 14 = 33 / 14 ~= 2,36

**If s/n > b rehashing will be performed**

Figure 2. find operation time complexity for hash table - initial n = 10 and b = 20

## Open addressing hash table

A hash table that is based on open addressing technique uses 1D array. Empty field is marked as -1.

| 0  | 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9  |
|----|----|----|----|----|----|----|----|----|----|
| -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 |

hashing function formula: h(element) = (element + i) % len(array), i = 0, 1, 2, 3, ... len(array) - 1

Open addressing implementation uses -1 value to mark field as deleted - this field is recognized as empty field.

| 0  | 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9  |
|----|----|----|----|----|----|----|----|----|----|
| -1 | -1 | -1 | -1 | -1 | -1 | -1 | -2 | -1 | -1 |

### Open addressing - scan_for utility method

scan_for method is used for finding element in array. scan_for returns array index where element is stored - if element is present in array or index where element may be inserted. If there is no spece left method returns -1.

- find first available place for element = 5 and insert
1. key = 5 % 10 # <- 5
2. check if array[key = 5] is empty (-1)
3. array[key = 5] is empty - return index = 5
4. array[5] = 5

| 0  | 1  | 2  | 3  | 4  | 5     | 6  | 7  | 8  | 9  |
|----|----|----|----|----|-------|----|----|----|----|
| -1 | -1 | -1 | -1 | -1 | **5** | -1 | -2 | -1 | -1 |

- find first available place for element = 7 and insert
1. key = 7 % 10 # <- 7
2. check if array[key = 7] is empty (-1)
3. check if array[key = 7] is deleted (-2)
4. array[-2] is deleted - save this index # deleted = 7
5. key = (7 + 1) % 10 # <- 8
6. check if array[key = 8] is empty (-1)
7. array[8] is empty
8. check if deleted != -1 # deleted = 7
9. return deleted 
10. array[7] = 7

| 0  | 1  | 2  | 3  | 4  | 5     | 6  | 7     | 8  | 9  |
|----|----|----|----|----|-------|----|-------|----|----|
| -1 | -1 | -1 | -1 | -1 | **5** | -1 | **7** | -1 | -1 |

Figure 1. find operation time complexity for open addressing

Figure 2. find operation time complexity for open addressing with rehashing if s\n >= 0.7
