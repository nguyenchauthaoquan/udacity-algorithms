import math
from random import randint


def rotate_list(list: []) -> []:
    if not list:
        return []

    pivot_index = randint(0, len(list) - 1)

    output = list[pivot_index:] + list[:pivot_index]

    return output


def rotated_array_search(input_list, number):
    rotated_list = rotate_list(input_list)

    return search(list=rotated_list, value=number, type="meta binary")


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

    if right_index <= 0:
        return -1
    else:
        while left_index <= right_index:
            mid_index = left_index + (right_index - left_index) // 2

            if list[mid_index] == value:
                return mid_index
            elif list[mid_index] < value:
                left_index = mid_index + 1
            else:
                right_index = mid_index - 1


def meta_binary_search(list: [], value: int) -> int:
    n = len(list)
    interval_size = int(math.log2(n - 1)) + 1
    index = 0

    for i in range(interval_size - 1, -1, -1):
        if list[index] == value:
            return index
        new_index = index | (1 << i)

        if (new_index < n) and (list[new_index] <= value):
            index = new_index

    return index if list[index] == value else -1
