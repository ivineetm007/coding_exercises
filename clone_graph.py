"""
This is a problem on leetcode.com
https://leetcode.com/problems/clone-graph/

------------------------
Problem statement
------------------------
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

Constraints:

The number of nodes in the graph is in the range [0, 100].
1 <= Node.val <= 100
Node.val is unique for each node.
There are no repeated edges and no self-loops in the graph.
The Graph is connected and all nodes can be visited starting from the given node.

--------------------
Solution1
--------------------
Pre-requisite
Deep copy in python
    1. Creating a new object of class will have new address and memory.
    2. Suppose, class has a member which stores a list say "lt"
        2.1 We have two class objects A and B, if we assign A.lt= [1,2,3] a


 Step1. Create copy of all nodes
    Traverse the graph and create a hashmap- 
        key: original node value (**Node values are unique as per the constraints) 
        VALUE: original node and duplicate node address/pointer tuple 
        
 Step2. Connect edges in the duplicate graph.
    Iterate over the hasmap. For each node pair
        Iterate over all edges of original node and create similar edges in the duplicate node

Time Complexity: Two times graph traveral-> 2(V+E)
Space complexity: V+E for duplicate graph, O(V) for hashmap

"""

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from collections import deque
class Solution:
    def cloneGraph(self, node: Node) -> Node:
        if node == None:
            return None
        #Create nodes
        node_lookup = {}
        node_lookup[node.val] = None
        traverse_q = deque()
        traverse_q.append(node)
        while(traverse_q):
            temp = traverse_q.popleft()
            for neigh in temp.neighbors:
                if neigh.val not in node_lookup:
                    traverse_q.append(neigh)
                    node_lookup[neigh.val] = None
            dup = Node(temp.val)
            node_lookup[temp.val] = (temp, dup)
        #create edges
        for val, node_pair in node_lookup.items():
            orig, dup = node_pair
            for neigh in orig.neighbors:
                dup.neighbors.append(node_lookup[neigh.val][1])
                
        return node_lookup[1][1]
