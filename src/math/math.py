import math


class Math:
    @staticmethod
    def sqrt(n: int) -> int:
        """
        Calculate the floored square root of a number
        @param n: Number to find the floored squared root
        @return: Floored Square Root
        """
        if n >= 0:
            result = 0
            start_number = 0
            end_number = n

            while start_number <= end_number:
                mid_number = start_number + (end_number - start_number) // 2

                if int(math.pow(mid_number, 2)) == n:
                    return mid_number
                elif int(math.pow(mid_number, 2)) < n:
                    start_number = mid_number + 1
                    result = mid_number
                else:
                    end_number = mid_number - 1

            return result
