import random

from src.list.list import rotate_list, search, rotated_array_search, merge_sort, insertion_sort, tim_sort, \
    rearrange_digits

if __name__ == '__main__':
    input_list = [0, 1, 2, 4, 5, 6, 7]
    print("Input list:", input_list)
    print("Problem 2: ", rotated_array_search(input_list, 4))
    print("Problem 3: ", rearrange_digits([4, 6, 2, 5, 9, 8]))
