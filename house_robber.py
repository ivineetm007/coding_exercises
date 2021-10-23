"""
This is a problem on leetcode.com
https://leetcode.com/problems/house-robber/

Problem statement
-----------------------
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

Solutions
----------------------------------------
Wrong solution
--------------
Take max of sum of odd elements and even elements.
Counterexmple
[1,2,3,1,1,100]
Even- 2+1+100 = 103
Odd- 1+3+1 = 5
Best- 1+3+100 = 104

DP solution
----------------------
A-> array, s-> solution array
Recursion
S[N]= max(S[N-1],S[N-2]+A[N])
Initiate S with 0
Iterate in bottom-up fashion i.e 1 to N
"""
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        robList=[0]*(n+1)
        robList[0]=0
        robList[1]=nums[0] 
        for i in range(2,n+1):
            robList[i]= max(robList[i-1], robList[i-2]+nums[i-1])
        return robList[n]

if __name__ == '__main__':
    sol = Solution()
    #Simple cases
    assert sol.rob([2,7,9,3,1]) == 12
    assert sol.rob([1,2,3,1,1,100]) == 104
    #Edge cases   
    assert sol.rob([1]) == 1
    print("B-)")
        