"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates
in-place such that each unique element appears only once. The relative order of
the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k. To get accepted, you need to:
- Change the array nums such that the first k elements of nums contain the unique elements
  in the order they were present in nums initially.
- The remaining elements of nums are not important.
- Return k.

Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]

Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
"""

from typing import List
import unittest


class Solution:
    # Time complexity: O(n)
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        return k


class TestRemoveDuplicates(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 1, 2]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, 2)
        self.assertEqual(nums[:k], [1, 2])

    def test_example_2(self):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, 5)
        self.assertEqual(nums[:k], [0, 1, 2, 3, 4])

    def test_single_element(self):
        nums = [1]
        k = self.solution.removeDuplicates(nums)
        self.assertEqual(k, 1)
        self.assertEqual(nums[:k], [1])


if __name__ == "__main__":
    unittest.main()
