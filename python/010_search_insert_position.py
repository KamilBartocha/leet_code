"""
Given a sorted array of distinct integers and a target value, return the index
if the target is found. If not, return the index where it would be if it were
inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4
"""

from typing import List
import unittest


class Solution:
    # Time complexity: O(log n)
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left


class TestSearchInsertPosition(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.searchInsert([1, 3, 5, 6], 5), 2)

    def test_example_2(self):
        self.assertEqual(self.solution.searchInsert([1, 3, 5, 6], 2), 1)

    def test_example_3(self):
        self.assertEqual(self.solution.searchInsert([1, 3, 5, 6], 7), 4)

    def test_insert_at_start(self):
        self.assertEqual(self.solution.searchInsert([1, 3, 5, 6], 0), 0)

    def test_single_element_found(self):
        self.assertEqual(self.solution.searchInsert([1], 1), 0)


if __name__ == "__main__":
    unittest.main()
