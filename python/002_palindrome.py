"""Given an integer x, return true if x is a palindrome, and false otherwise."""

import unittest


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return str(x) == str(x)[::-1]


class TestIsPalindrome(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.isPalindrome(121), True)

    def test_example_2(self):
        self.assertEqual(self.solution.isPalindrome(-121), False)

    def test_example_3(self):
        self.assertEqual(self.solution.isPalindrome(10), False)


if __name__ == "__main__":
    unittest.main()
