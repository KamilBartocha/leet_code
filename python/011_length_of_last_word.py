"""
Given a string s consisting of words and spaces, return the length of the
last word in the string.

A word is a maximal substring consisting of non-space characters only.

Example 1:
Input: s = "Hello World"
Output: 5

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
"""

import unittest


class Solution:
    # Time complexity: O(n)
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rstrip().split(" ")[-1])


class TestLengthOfLastWord(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.lengthOfLastWord("Hello World"), 5)

    def test_example_2(self):
        self.assertEqual(self.solution.lengthOfLastWord("   fly me   to   the moon  "), 4)

    def test_example_3(self):
        self.assertEqual(self.solution.lengthOfLastWord("luffy is still joyboy"), 6)

    def test_single_word(self):
        self.assertEqual(self.solution.lengthOfLastWord("day"), 3)


if __name__ == "__main__":
    unittest.main()
