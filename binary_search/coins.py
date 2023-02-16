"""
This module is a solution for the problem in the following link:
https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/bags-of-coins-7b1d612c/

Problem
There are N bags and each bag contains some coin(s). Your task is to select an integer X and remove all the bags
in which the number of coins is equal to X. Divide the remaining bags into two non-empty groups such that:

 1. The number of coin(s) in each bag of the first group is strictly smaller than X.
 2. The number of coin(s) in each bag of the second group is strictly larger than X.
 3. The total number of coins of one group is equal to the other.

"""

from enum import Enum
from typing import List


class ComparisonResult(Enum):
    SMALLER = -1
    EQUAL = 0
    BIGGER = 1
    ALL_EQUAL = -2


class CoinProblemSolver:
    def __init__(self, number_of_bags: int, bags_contents: List[int]):
        self.__number_of_bags = number_of_bags
        self.__bags_contents = bags_contents

    def solve(self) -> bool:
        low = min(self.__bags_contents)
        high = max(self.__bags_contents)

        while low <= high:
            mid = (high + low) // 2
            compare_result: ComparisonResult = self.__compare_summation_of_two_halves(mid)
            if compare_result == ComparisonResult.EQUAL:
                return True

            elif compare_result == ComparisonResult.SMALLER:
                low = mid + 1
            else:
                high = mid - 1

        return False

    def __compare_summation_of_two_halves(self, mid: int) -> ComparisonResult:
        mid_item = mid

        sum_of_first_half = 0
        sum_of_second_half = 0
        for idx, item in enumerate(self.__bags_contents):
            if item < mid_item:
                sum_of_first_half = sum_of_first_half + item
            if item > mid_item:
                sum_of_second_half = sum_of_second_half + item

        if sum_of_first_half == sum_of_second_half == 0:
            return ComparisonResult.ALL_EQUAL

        elif sum_of_first_half == sum_of_second_half:
            return ComparisonResult.EQUAL

        elif sum_of_first_half < sum_of_second_half:
            return ComparisonResult.SMALLER

        elif sum_of_first_half > sum_of_second_half:
            return ComparisonResult.BIGGER


if __name__ == "__main__":
    n = int(input())
    list_string = input().split()
    input_bags_contents = [int(x) for x in list_string]

    result = CoinProblemSolver(number_of_bags=n, bags_contents=input_bags_contents).solve()
    if result:
        print("YES")
    else:
        print("NO")
