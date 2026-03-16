"""
Given two strings haystack and needle, return the index of the first occurrence
of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6. The first occurrence is at index 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode".
"""

import unittest


class Solution:
    # Time complexity: O(n * m)
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        for i in range(n - m + 1):
            if haystack[i:i + m] == needle:
                return i
        return -1


class TestFindIndexOfFirstOccurrence(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.strStr("sadbutsad", "sad"), 0)

    def test_example_2(self):
        self.assertEqual(self.solution.strStr("leetcode", "leeto"), -1)

    def test_empty_needle(self):
        self.assertEqual(self.solution.strStr("hello", ""), 0)

    def test_needle_equals_haystack(self):
        self.assertEqual(self.solution.strStr("abc", "abc"), 0)

    def test_needle_at_end(self):
        self.assertEqual(self.solution.strStr("hello", "lo"), 3)


if __name__ == "__main__":
    unittest.main()
