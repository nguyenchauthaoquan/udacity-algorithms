from src.list.list import rotated_array_search, rearrange_digits, count_sort, rotate_list, sort_012

if __name__ == '__main__':
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 1000]
    print("Input list:", input_list)
    print(rotate_list(input_list))
    print("Problem 2: ", rotated_array_search(input_list, 1000))
    print("Problem 3: ", rearrange_digits([4, 6, 2, 5, 9, 8]))
    print("Problem 4: ", sort_012([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1, 1]))
