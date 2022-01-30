"""
This is a problem on leetcode.com

https://leetcode.com/problems/minimum-depth-of-binary-tree/

------------------------
Problem statement
------------------------
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
--------------
Solution1
--------------
Traverse all nodes
    If node is leaf node
        check/update min_depth

--------------
Solution2
--------------
Recurisve solution
MinDepth = 1 + min(node.child1,node.child2, node.child3...) where node.child{i} is not None

**Don;t call recursively for None nodes
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        min_depth = float('inf')
        if root.left:
            l = self.minDepth(root.left)
            min_depth = min(min_depth,l)
        if root.right:
            r = self.minDepth(root.right)
            min_depth = min(min_depth,r)
        
        return 1+min_depth