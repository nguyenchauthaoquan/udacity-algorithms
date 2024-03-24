import math

from src.math.math import Math

if __name__ == '__main__':
    print("Calculate sqrt with O(1) complexity")
    print(25 ** 0.5)
    print("Calculate sqrt using math built-in function")
    print(math.sqrt(25))
    print(math.sqrt(27))
    print("Calculate sqrt using binary search")
    print(Math.sqrt(25))
    print(Math.sqrt(27))