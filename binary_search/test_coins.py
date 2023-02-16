from dataclasses import dataclass
from typing import List
from unittest import TestCase

from binary_search.coins import CoinProblemSolver


@dataclass
class _TestData:
    number_of_bags: int
    bags_contents: List[int]
    result: bool


class TestCoins(TestCase):
    def test_1(self):
        test_data = [
            _TestData(5, [1, 1, 2, 3, 4], True),
            _TestData(10, [4, 4, 4, 4, 4, 4, 6, 6, 6, 6], True),
            _TestData(4, [1, 1, 2, 4], True),
            _TestData(6, [1, 1, 1, 1, 1, 1], False),
            _TestData(6, [1, 1, 2, 2, 3, 4], False),
            _TestData(5, [1, 1, 2, 3, 4], True),
            _TestData(4, [1, 1, 1, 1], False),
            _TestData(5, [99669, 99074, 99262, 99609, 99407], False),
        ]

        for td in test_data:
            result = CoinProblemSolver(number_of_bags=td.number_of_bags, bags_contents=td.bags_contents).solve()
            self.assertEqual(result, td.result, msg=td)
