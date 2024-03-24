from src.list.list import rotate_list, search, rotated_array_search

if __name__ == '__main__':
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Input list:", input_list)
    output_list = rotate_list(input_list)
    print("Randomly rotated list:", output_list)
    print("Linear search result: ", search(input_list, 6))
    print("Sentinel linear search result: ", search(input_list, 8, type="sentinel linear"))
    print("Binary search result: ", search(input_list, 7, type="binary"))
    print("Meta binary search result: ", search(input_list, 1, type="meta binary"))

    input_list = [0, 1, 2, 4, 5, 6, 7]
    print("Input list:", input_list)
    print("Rotated array search result: ", rotated_array_search(input_list, 1))