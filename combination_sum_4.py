"""
This is a problem on leetcode.com
https://leetcode.com/problems/combination-sum-iv/submissions/

------------------------
Problem statement
------------------------
Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The answer is guaranteed to fit in a 32-bit integer.


Example 1:

Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.
Example 2:

Input: nums = [9], target = 3
Output: 0

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 1000
All the elements of nums are unique.
1 <= target <= 1000

------------------
Solutions
------------------
Considerations:-
1. We can choose an element any number of times from the given nums array.
2. As we can see in the first example, we need to calculate all number of possible permutations. (not combinations (1,3) and (3,1) would be same in that case)

-----------------
Solution1
-----------------
Step 1 Sort the numbers in the given array "nums"
Step 2 Recursion Structure/definition
    If nums is all natural numbers, then T(N)= Sum(T(N-i))  i=>1 to N, which would be equal to 2^(N-1), T(0)=1
    In general, T(N)= Sum(T(N-i)) i is selected from nums and i<=N
Step 3 Directly using Bottom-up approach
    Iterate from 1 to Target or T; find and store the number of combinations for all the subproblems.

Analysis
len(nums) = N
Target = T

Time complexity= time to sort and dp solution= O(NlogN + NT)
Space compexlity= T
"""
from typing import List
class Solution1:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()#Nlog(N)
        if target<nums[0]:
            return 0
        count_comb = [0 for i in range(target+1)]# O(T)
        count_comb[0] = 1
        for num in range(nums[0], target+1):
            for first_len in nums:
                if first_len>num:
                    break
                count_comb[num]+=count_comb[num-first_len]
        return count_comb[target]