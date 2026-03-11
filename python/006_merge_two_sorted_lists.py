"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by
splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
"""

from typing import Optional
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Time complexity: O(n + m)
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        current.next = list1 if list1 else list2
        return dummy.next


def list_to_linked(values):
    dummy = ListNode()
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next


def linked_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


class TestMergeTwoSortedLists(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        l1 = list_to_linked([1, 2, 4])
        l2 = list_to_linked([1, 3, 4])
        self.assertEqual(linked_to_list(self.solution.mergeTwoLists(l1, l2)), [1, 1, 2, 3, 4, 4])

    def test_example_2(self):
        self.assertEqual(linked_to_list(self.solution.mergeTwoLists(None, None)), [])

    def test_example_3(self):
        l2 = list_to_linked([0])
        self.assertEqual(linked_to_list(self.solution.mergeTwoLists(None, l2)), [0])


if __name__ == "__main__":
    unittest.main()
