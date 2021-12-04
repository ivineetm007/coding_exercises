"""
This is a problem on leetcode.com

https://leetcode.com/problems/convert-bst-to-greater-tree/

------------------------
Problem statement
------------------------

Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

------------------------
Solutions
------------------------
Solution1
Write a recursive function for a node:-
    1. It will return the sum of whole BST from node
    2. We will send the rightSum that we get from parent node to this function.
    3. node.val = node.val + rightTreeSum + rightSumParent


Solution2
Just use one variable sum instead of rightTreeSum and rightSumParent

"""
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution1:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recursiveGreaterTree(node, rightSumParent=0):
            if node==None:
                return 0
            rightSum = recursiveGreaterTree(node.right, rightSumParent=rightSumParent)
            nodeOrgVal = node.val
            node.val = node.val + rightSum + rightSumParent
            leftSum = recursiveGreaterTree(node.left, rightSumParent=node.val)
            return nodeOrgVal + leftSum + rightSum
            
        recursiveGreaterTree(root)
        return root


class Solution2:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recursiveGreaterTree(node, sum_=0):
            if node==None:
                return sum_
            sum_ = recursiveGreaterTree(node.right, sum_)
            node.val = node.val + sum_
            sum_ = node.val
            sum_ = recursiveGreaterTree(node.left, sum_)
            return sum_
        recursiveGreaterTree(root)
        return root
        