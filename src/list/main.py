import random

from src.list.list import rotate_list, search, rotated_array_search, merge_sort, insertion_sort, tim_sort

if __name__ == '__main__':
    input_list = [i for i in range(0, 100)]
    print("Input list:", input_list)
    print("Input list items:", len(input_list))
    output_list = rotate_list(input_list)
    print("Randomly rotated list:", output_list)
    print("Linear search result: ", search(input_list, 6))
    print("Sentinel linear search result: ", search(input_list, 8, type="sentinel linear"))
    print("Binary search result: ", search(input_list, 7, type="binary"))
    print("Meta binary search result: ", search(input_list, 1, type="meta binary"))
    print("Input list:", input_list)
    print("Rotated array search result: ", rotated_array_search(input_list, 1))
    print("Sorting the list in ascending order")
    print("Insertion sort: ", insertion_sort(input_list, comparator=lambda x,y: x < y))
    print("Merge sort: ", merge_sort(input_list, comparator=lambda x,y: x < y))
    print("Tim sort: ", tim_sort(input_list, comparator=lambda x,y: x < y))

    print("Sorting the list in descending order")
    print("Insertion sort: ", insertion_sort(input_list, comparator=lambda x, y: x > y))
    print("Merge sort: ", merge_sort(input_list, comparator=lambda x, y: x > y))
    print("Tim sort: ", tim_sort(input_list, comparator=lambda x, y: x > y))

