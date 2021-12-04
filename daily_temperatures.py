"""
This is a problem on leetcode.com

https://leetcode.com/problems/daily-temperatures/submissions/


Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

------------------------
Problem statement
------------------------

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100

------------------------
Solutions
------------------------
Solution1

Use stack

"""
from typing import List
class Solution1:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0]*n
        temp_stack = []
        ind=0
        while(ind<n):
            next_val = temperatures[ind]
            while( temp_stack and temperatures[temp_stack[-1]]<next_val):
                answer[temp_stack[-1]] = ind-temp_stack[-1]
                temp_stack.pop()
            temp_stack.append(ind)
            ind+=1
        return answer
        
        