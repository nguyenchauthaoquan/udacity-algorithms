# Project: Udacity Problems and Algorithms

Both project 3 and project 4 are mainly focus the algorithm, and for the convenient, I will use this repository to implement both project.

## Project 3: Problems vs. Algorithms

For this project, you will answer the seven questions laid out in the next sections. The questions cover a variety of topics related to the basic algorithms you've learned in this course. You will write up a clean and efficient answer in Python, as well as a text explanation of the efficiency of your code and your design choices.

### Problem 1: Square Root of an Integer

This problem is to find the square root of the integer without using any Python library. You have to find the floor value of the square root.
For example if the given number is 16, then the answer would be 4.

If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.
Although there are many solutions to implement this problem faster, but the expected time complexity is `O(log(n))`, so to achieve the `O(log(n))`, I will use the binary search solution to find the square root of number.

Here is the code in math.py of math folder
```python
def sqrt(n: int) -> int:
    """
    Time complexity: O(log(n))
    Space complexity: O(1)
    """
    import math
    if n >= 0:
        result = 0 # This is the result of the square root
        # Set the range from 0 to n by setting 2 point to shallow the searching with the binary search
        start_number = 0 # This is the starting point
        end_number = n # This is the ending point
        
        # Begin binary search
        while start_number <= end_number: # O(log(n))
            mid_number = start_number + (end_number - start_number) // 2
            # if mid_number^ 2 is n, then get the middle point
            if int(math.pow(mid_number, 2)) == n:
                return mid_number
            # if mid_number^ 2 less than n, extends the starting point then set the middle point
            elif int(math.pow(mid_number, 2)) < n:
                start_number = mid_number + 1
                result = mid_number
            # if mid_number^ 2 greater than n, narrow the ending point
            else:
                end_number = mid_number - 1

            return result
```

### Problem 2: Search in a Rotated Sorted Array

You are given a sorted array which is rotated at some random pivot point.

Example: `[0,1,2,4,5,6,7]` might become `[4,5,6,7,0,1,2]`

You are given a target value to search. If found in the array return its index, otherwise return -1.

You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of `O(log n)`.

we can use the binary sort directly for this solution, unlike the problem 1, we can initialize the left and right points directly with the specific items in the array
left is the first item, right is the last item in the list/array
Here is the code in list.py of list folder
```python
from random import randint
def rotate_list(list: []) -> []:
    """
    Time complexity: O(n)
    Space complexity: O(n) for create the rotated list in line 69
    """
    if not list:
        return []

    pivot_index = randint(0, len(list) - 1)

    list[:] = list[pivot_index:] + list[:pivot_index] # O(n)

    return list


def rotated_array_search(input_list, number):
    """
    Time complexity: O(log(n))
    Space complexity: O(n)
    """
    rotated_list = rotate_list(input_list) # O(n)

    return binary_search(list=rotated_list, value=number) # O(log(n))

def binary_search(list: [], value: int) -> int:
    """
    Time complexity: O(log(n))
    Space complexity: O(1)
    """
    left_index = 0
    right_index = len(list) - 1

    while left_index <= right_index: # O(log(n))
        middle_index = (left_index + right_index) // 2
        if list[middle_index] == value:
            return middle_index

        # If arr[left:mid] is sorted, narrow the right side or extend the left side
        if list[left_index] <= list[middle_index]:
            # If the target is within the sorted range (left and middle index), narrow the right side, otherwise, extend the left side
            if list[left_index] <= value < list[middle_index]:
                right_index = middle_index - 1
            else:
                left_index = middle_index + 1
        # If arr[mid:right] is sorted
        else:
            # If the target is within the sorted range (middle and right index), extends the left side, otherwise, narrow the right side
            if list[middle_index] < value <= list[right_index]:
                left_index = middle_index + 1
            else:
                right_index = middle_index - 1
    return -1 # in case not found
```

### Problem 3: Rearrange Array Digits

Rearrange Array Elements to form two number such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is `O(nlog(n))`.

The expected answer would be `[531, 42]`. Another expected answer can be `[542, 31]`. In scenarios such as these when there are more than one possible answers, return any one.

I used the following code implemented in list.py of list folder:

```python
TIM_SORT_MIN_SIZE = 32
def rearrange_digits(input_list):
    """
    Time complexity: O(nlog(n)) due to tim sort processing
    Space complexity: O(n) due to tim sort processing
    """
    max_sum_number1 = 0
    max_sum_number2 = 0
    sorted_input_list = tim_sort(input_list, comparator=lambda x, y: x > y)

    for i in range(0, len(sorted_input_list), 2):
        max_sum_number1 = max_sum_number1 * 10 + sorted_input_list[i]

    for j in range(1, len(sorted_input_list), 2):
        max_sum_number2 = max_sum_number2 * 10 + sorted_input_list[j]

    return max_sum_number1, max_sum_number2


def insertion_sort(list: [], comparator=lambda x, y: x < y) -> []:
    """
    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    if len(list) > 1:
        for i in range(1, len(list)):# O(n)
            key = list[i]

            current_index = i - 1

            while current_index >= 0 and comparator(key, list[current_index]): # O(n)
                list[current_index + 1] = list[current_index]
                current_index -= 1
            list[current_index + 1] = key
        return list
    else:
        return []


def merge_sort(list: [], comparator=lambda x, y: x < y) -> []:
    """
    Time complexity: O(nlog(n))
    Space complexity: O(n) for partitioning the new space during merging the sub sorted list
    """
    if len(list) > 1:
        mid_index = len(list) // 2
        left_items = list[:mid_index]
        right_items = list[mid_index:]

        merge_sort(left_items, comparator)
        merge_sort(right_items, comparator)

        left_index = right_index = main_index = 0

        while left_index < len(left_items) and right_index < len(right_items):
            if comparator(left_items[left_index], right_items[right_index]):
                list[main_index] = left_items[left_index]
                left_index += 1
            else:
                list[main_index] = right_items[right_index]
                right_index += 1
            main_index += 1

        while left_index < len(left_items):
            list[main_index] = left_items[left_index]
            left_index += 1
            main_index += 1

        while right_index < len(right_items):
            list[main_index] = right_items[right_index]
            right_index += 1
            main_index += 1

        return list
    else:
        return []

def tim_sort(list: [], comparator=lambda x, y: x < y):
    """
    Time complexity: O(n^2) for best case due to insertion sort only, O(nlog(n)) for merge sort after insertion sort
    Space complexity: O(n) for sorting with both insertion sort and merge sort
    """
    sorted_list = []
    for i in range(0, len(list), TIM_SORT_MIN_SIZE):
        sorted_list = insertion_sort(list[i: min((i + TIM_SORT_MIN_SIZE), len(list))], comparator)

    size = TIM_SORT_MIN_SIZE

    while size < len(list):
        for left_index in range(0, len(list), 2 * size):
            middle_index = left_index + size
            right_index = min((left_index + 2 * size), len(list))
            if middle_index < right_index:
                sorted_list = merge_sort(list[left_index: right_index], comparator)

        size *= 2

    return sorted_list


```

### Problem 4: Dutch National Flag Problem

Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.

Note: O(n) does not necessarily mean single-traversal. For e.g. if you traverse the array twice, that would still be an `O(n)` solution but it will not count as single traversal.

I used the following code implemented in list.py of list folder:

```python
def find_min_max(input_list):
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    if len(input_list) == 0:
        return 0, 0
    min_element, max_element = input_list[0], input_list[0]

    for i in input_list: # O(n)
        if min_element > i:
            min_element = i
        if max_element < i:
            max_element = i

    return min_element, max_element

def sort_012(input_list):
    """
    Time complexity: O(n) due to count sort process
    Space complexity: O(n) due to count sort process
    """
    interested_values = [0, 1, 2]

    # If any value different from 0, 1, 2, return the empty list
    for value in input_list: # O(n)
        if value not in interested_values:
            return []

    return count_sort(input_list)

def count_sort(list: []):
    """
    Assume n is the size of sorted list and m is the size of counting list
    Time complexity: O(n + m) ~= O(n) due to count sort process
    Space complexity: O(n + m) ~= O(n)
    """
    _, max_element = find_min_max(list)
    count_list = [0] * (max_element + 1)

    for item in list: # O(m)
        count_list[item] += 1

    for i in range(1, max_element + 1):# O(m)
        count_list[i] += count_list[i - 1]
    sorted_list = [0] * len(list)

    for i in range(len(list) - 1, -1, -1): # O(n + m)
        sorted_list[count_list[list[i]] - 1] = list[i]
        count_list[list[i]] -= 1

    return sorted_list
```

### Problem 5: Autocomplete with Tries

In this problem, I don't use the skeleton in project workspace, here is the following implementation I have create the trie tree for a word:

```python
class TrieNode:
    def __init__(self, word=''):
        self.word = word
        self.children = {}
        self.is_word = False

class TrieTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Time complexity: O(n) for adding each character of the word into trie tree
        Space complexity: O(n)
        """
        current_node = self.root

        for i, char in enumerate(word):
            if char not in current_node.children: # add character into children if the parent have no child
                current_node.children[char] = TrieNode(word=word[:i + 1]) # Append children each character
            current_node = current_node.children[char]
        current_node.is_word = True

    def find(self, prefix):
        current_node = self.root

        for char in prefix:
            if char not in current_node.children:
                return None
            else:
                current_node = current_node.children[char]

        return current_node

    def get_suffixes(self, prefix, suffix=''):
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        current_node = self.root

        # Traverse the Trie to the end of the prefix
        for char in prefix: # O(n)
            if char not in current_node.children:
                return []

            current_node = current_node.children[char]

        # Collect suffixes recursively
        suffixes = []
        self._get_suffixes(current_node, suffixes) # O(n)
        return [suffix + word[len(prefix):] for word in suffixes] # O(n)

    def _get_suffixes(self, node, suffixes):
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        if node.is_word:
            suffixes.append(node.word)

        for child in node.children.values(): # O(n)
            self._get_suffixes(child, suffixes) 
```

### Problem 6: Unsorted Integer Array

### Problem 7: Request Routing in a Web Server with a Trie

## Project 4: Route Planner