"""
This is a problem on leetcode.com
https://leetcode.com/problems/triangle/

Problem statement
-----------------------

Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.
"""
from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        H = len(triangle)
        min_mem = triangle[-1].copy()
        
        for h in range(H-1,0,-1):
            for ind in range(h):
                min_mem[ind] = triangle[h-1][ind]+min(min_mem[ind],min_mem[ind+1])
        return min_mem[0]