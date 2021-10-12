"""
This is a problem on leetcode.com
https://leetcode.com/problems/search-insert-position/

Problem statement:-
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1


Corner case 1:
Input: nums = [1,3,5,6], target = 7
Output: 4

Corner case 2:
Input: nums = [1], target = 0
Output: 0

Corner case 3:
Input: nums = [1], target = 1
Output: 0

"""
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left= 0
        right= len(nums)-1
        while(right>left):
            mid = int((left+right)/2 )
            if(nums[mid]==target):
                return mid
            elif(nums[mid]<target):
                left = mid +1
            else:
                right= mid
        if(nums[left]>=target):
            return left
        else:
            return left+1
        

if __name__ == '__main__':
    sol = Solution()
    assert sol.searchInsert([1], 0) == 0
    assert sol.searchInsert([1], 1) == 0
    assert sol.searchInsert([1], 2) == 1
    print("B-)")