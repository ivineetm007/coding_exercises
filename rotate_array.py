"""
This is a problem on leetcode.com
https://leetcode.com/problems/rotate-array/

Problem statement:-
Given an array, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Solution1:
Copy last k elements in a new array
Iterate and shift the rest of the elemnts  (right to left iteration)
Paste the last k to the initial position

TIME O(n)
SPACE O(k)->O(n)

Ex.
arr = [1,2,3,4,5,6,7]
k=2
last_k => [6,7]    nums[-k:]
Shift others => [1,2,1,2,3,4,5],  iterate starting from index 4 to 0 which will len(arr)-k-1 till 0
Copy the last_k => [6,7,1,2,3,4,5]


Best solution- Juggling method 
https://www.geeksforgeeks.org/array-rotation/
"""
from typing import List
class Solution1:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        if k==0:
            return
        last_k = nums[-k:]
        for ind in range(n-k-1,-1,-1):
            nums[ind+k] = nums[ind]
        nums[0:k] = last_k

        """
        Pythonic simple code
        """
        # k = k%n
        # nums = nums[-k:] + nums[:-k]

if __name__ == '__main__':
    sol = Solution1()
    nums = [1,2,3,4,5,6,7]
    sol.rotate(nums, 3)
    assert nums == [5,6,7,1,2,3,4]
    nums = [1,2,3,4,5,6,7]
    sol.rotate(nums, 8)
    assert  nums == [7,1,2,3,4,5,6]
    nums = [1,2,3,4,5,6,7]
    sol.rotate(nums, 0)
    assert  nums == [1,2,3,4,5,6,7]
    print("B-)")