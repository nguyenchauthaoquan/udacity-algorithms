import math
from random import randint

TIM_SORT_MIN_SIZE = 32


def rotate_list(list: []) -> []:
    if not list:
        return []

    pivot_index = randint(0, len(list) - 1)

    list[:] = list[pivot_index:] + list[:pivot_index]

    return list


def rotated_array_search(input_list, number):
    rotated_list = rotate_list(input_list)

    print(rotated_list)

    return search(list=rotated_list, value=number, type="binary")


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.
    Args:
        input_list(list): Input List
    Returns:
        (int),(int): Two maximum sums
    """
    max_sum_number1 = 0
    max_sum_number2 = 0
    sorted_input_list = tim_sort(input_list, comparator=lambda x, y: x > y)

    for i in range(0, len(sorted_input_list), 2):
        max_sum_number1 = max_sum_number1 * 10 + sorted_input_list[i]

    for j in range(1, len(sorted_input_list), 2):
        max_sum_number2 = max_sum_number2 * 10 + sorted_input_list[j]

    return max_sum_number1, max_sum_number2


def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    pass


def find_min_max(input_list):
    min_element, max_element = 0, 0

    for i in input_list:
        if min_element > i:
            min_element = i
        if max_element < i:
            max_element = i

    return min_element, max_element


def search(list: [], value: int, type: str = "linear") -> int:
    if type == "linear":
        return linear_search(list, value)
    elif type == "sentinel linear":
        return sentinel_linear_search(list, value)
    elif type == "binary":
        return binary_search(list, value)
    elif type == "meta binary":
        return meta_binary_search(list, value)
    else:
        raise ValueError()


def linear_search(list: [], value: int) -> int:
    for i in range(len(list)):
        if list[i] == value:
            return i
    return -1


def sentinel_linear_search(list, value):
    last_item = list[len(list) - 1]
    list[len(list) - 1] = value

    i = 0

    while list[i] != value:
        i += 1

    list[i] = last_item

    if (i < len(list) - 1) or (list[len(list) - 1] == value):
        return i
    else:
        return -1


def binary_search(list: [], value: int) -> int:
    left_index = 0
    right_index = len(list) - 1

    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2
        if list[middle_index] == value:
            return middle_index

        # If arr[left:mid] is sorted
        if list[left_index] <= list[middle_index]:
            # If the target is within the sorted range
            if list[left_index] <= value < list[middle_index]:
                right_index = middle_index - 1
            else:
                left_index = middle_index + 1
        # If arr[mid:right] is sorted
        else:
            # If the target is within the sorted range
            if list[middle_index] < value <= list[right_index]:
                left_index = middle_index + 1
            else:
                right_index = middle_index - 1
    return -1


def meta_binary_search(list: [], value: int) -> int:
    n = len(list)
    interval_size = int(math.log(n - 1, 2.0)) + 1
    index = 0

    for i in range(interval_size - 1, -1, -1):
        if list[index] == value:
            return index
        new_index = index | (1 << i)

        if new_index < n and list[new_index] <= value:
            index = new_index
    return index if list[index] == value else -1


def insertion_sort(list: [], comparator=lambda x, y: x < y) -> []:
    if len(list) > 1:
        for i in range(1, len(list)):
            key = list[i]

            current_index = i - 1

            while current_index >= 0 and comparator(key, list[current_index]):
                list[current_index + 1] = list[current_index]
                current_index -= 1
            list[current_index + 1] = key
        return list
    else:
        return []


def merge_sort(list: [], comparator=lambda x, y: x < y) -> []:
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


def count_sort(list: []):
    _, max_element = find_min_max(list)
    count_list = [0] * (max_element + 1)

    for item in list:
        count_list[item] += 1

    for i in range(1, max_element + 1):
        count_list[i] += count_list[i - 1]

    sorted_list = [0] * len(list)

    for i in range(len(list) - 1, -1, -1):
        sorted_list[count_list[list[i]] - 1] = list[i]
        count_list[list[i]] -= 1

    return sorted_list
