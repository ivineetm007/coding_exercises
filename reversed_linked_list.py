"""
This is a problem on leetcode.com
https://leetcode.com/problems/reverse-linked-list/

Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []

Solution1:
Use recursion to reverse the list
Call the function reverse until we reach the last node where we return last node itself (a single node is reversed itself.)

TIME O(n)
SPACE O(n) Due recursion function call stack


Better solution 
Improve space complexity.
Use three pointers to iterate over the list and reverse at the same time.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        def reverse(node):
            if node.next == None:
                return node, node
            next_node, reversed_head = reverse(node.next)
            next_node.next = node
            return node, reversed_head
        head, reversed_head = reverse(head)
        head.next = None
        return reversed_head