"""
Given an integer array nums and an integer val, remove all occurrences of val
in nums in-place. The order of the elements may be changed. Then return the
number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k.
To get accepted, you need to:
- Change the array nums such that the first k elements of nums contain the
  elements which are not equal to val.
- The remaining elements of nums are not important.
- Return k.

Example 1:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]

Example 2:
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
"""

from typing import List
import unittest


class Solution:
    # Time complexity: O(n)
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k


class TestRemoveElement(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [3, 2, 2, 3]
        k = self.solution.removeElement(nums, 3)
        self.assertEqual(k, 2)
        self.assertEqual(sorted(nums[:k]), [2, 2])

    def test_example_2(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        k = self.solution.removeElement(nums, 2)
        self.assertEqual(k, 5)
        self.assertEqual(sorted(nums[:k]), [0, 0, 1, 3, 4])

    def test_all_removed(self):
        nums = [1, 1, 1]
        k = self.solution.removeElement(nums, 1)
        self.assertEqual(k, 0)

    def test_none_removed(self):
        nums = [1, 2, 3]
        k = self.solution.removeElement(nums, 4)
        self.assertEqual(k, 3)


if __name__ == "__main__":
    unittest.main()
