"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

from typing import List
import unittest


class Solution:
    def longest_common_prefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix


class TestLongestCommonPrefix(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(
            self.solution.longest_common_prefix(["flower", "flow", "flight"]), "fl"
        )

    def test_example_2(self):
        self.assertEqual(
            self.solution.longest_common_prefix(["dog", "racecar", "car"]), ""
        )

    def test_example_3(self):
        self.assertEqual(self.solution.longest_common_prefix([]), "")


if __name__ == "__main__":
    unittest.main()
