"""
Given an array of integers nums and an integer target, return indices of the two
numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not
use the same element twice.
You can return the answer in any order.
"""

from typing import List
import unittest


class Solution:
    # Time complexity: O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_num_idx = {}
        for index, num in enumerate(nums):
            expected = target - num
            if expected not in map_num_idx.keys():
                map_num_idx[num] = index
            else:
                return [map_num_idx[expected], index]


class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.twoSum([2, 7, 11, 15], 9), [0, 1])

    def test_example_2(self):
        self.assertEqual(self.solution.twoSum([3, 2, 4], 6), [1, 2])

    def test_example_3(self):
        self.assertEqual(self.solution.twoSum([1, 1, 1, 1, 1, 1, 4, 1, 2], 6), [6, 8])


if __name__ == "__main__":
    unittest.main()
