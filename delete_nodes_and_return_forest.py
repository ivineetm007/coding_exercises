"""
This is a problem on leetcode.com
https://leetcode.com/problems/delete-nodes-and-return-forest/
------------------------
Problem statement
------------------------
Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest. You may return the result in any order.

 

Example 1:


Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
Example 2:

Input: root = [1,2,4,null,3], to_delete = [3]
Output: [[1,2,4]]
 

Constraints:

The number of nodes in the given tree is at most 1000.
Each node has a distinct value between 1 and 1000.
to_delete.length <= 1000
to_delete contains distinct values between 1 and 1000.
------------------------
Solutions
------------------------
Solution1
Do post order traversal, if node needs to be deleted, then it's children will be appended to the final_root_nodes list.
Since, it could be possible that child also needs to be deleted; we can return a flag whether the node will remain in the 
final tree or not. If it will not, we can skip appending it to the final list

Solution2
In the first solution, we sent a signal from child to parent, we can do reverse as well i.e parent sends a singal to child
 whether it's parent will be deleted or not


"""
# Definition for a binary tree node.
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        final_root_nodes = []
        def deleteTraversal(node):
            if not node:
                return False
            left_check = deleteTraversal(node.left)
            right_check = deleteTraversal(node.right)
            
            if node.val in to_delete:
                if(left_check):
                    final_root_nodes.append(node.left)
                if(right_check):
                    final_root_nodes.append(node.right)
                return False
            if(not left_check):
                node.left = None
            if(not right_check):
                node.right = None
            return True
        deleteTraversal(root)
        if root.val not in to_delete:
            final_root_nodes.append(root)
        return final_root_nodes

