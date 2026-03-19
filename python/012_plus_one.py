"""
You are given a large integer represented as an integer array digits, where
each digits[i] is the ith digit of the integer. The digits are ordered from
most significant to least significant in left-to-right order. Increment the
large integer by one and return the resulting array of digits.

Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]

Example 3:
Input: digits = [9]
Output: [1,0]
"""

from typing import List
import unittest


class Solution:
    # Time complexity: O(n)
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits


class TestPlusOne(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.plusOne([1, 2, 3]), [1, 2, 4])

    def test_example_2(self):
        self.assertEqual(self.solution.plusOne([4, 3, 2, 1]), [4, 3, 2, 2])

    def test_example_3(self):
        self.assertEqual(self.solution.plusOne([9]), [1, 0])

    def test_all_nines(self):
        self.assertEqual(self.solution.plusOne([9, 9, 9]), [1, 0, 0, 0])


if __name__ == "__main__":
    unittest.main()
