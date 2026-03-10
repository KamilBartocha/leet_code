"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
"""

import unittest


class Solution:
    # Time complexity: O(n)
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in mapping:
                top = stack.pop() if stack else '#'
                if mapping[char] != top:
                    return False
            else:
                stack.append(char)
        return not stack


class TestValidParentheses(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.isValid("()"), True)

    def test_example_2(self):
        self.assertEqual(self.solution.isValid("()[]{}"), True)

    def test_example_3(self):
        self.assertEqual(self.solution.isValid("(]"), False)

    def test_empty_string(self):
        self.assertEqual(self.solution.isValid(""), True)

    def test_nested(self):
        self.assertEqual(self.solution.isValid("{[()]}"), True)


if __name__ == "__main__":
    unittest.main()
