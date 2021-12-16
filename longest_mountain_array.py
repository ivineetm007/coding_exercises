"""
This is a problem on leetcode.com
https://leetcode.com/problems/longest-mountain-in-array/

Problem statement
-----------------------
You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given an integer array arr, return the length of the longest subarray, which is a mountain. Return 0 if there is no mountain subarray.

 

Example 1:

Input: arr = [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
Example 2:

Input: arr = [2,2,2]
Output: 0
Explanation: There is no mountain.
 

Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 104


------------------------
Solutions
------------------------
Properties
1. Two mountains cannot overlap. If a mountain is found from index 'start' till 'end'. We can iterate next from start=end to find next mountain.

Logic
1. Iterate and find a peak
2. If found a peak, iterate left and right to find it's length.
3. Keep track of the maximum length.

"""
from typing import List
class Solution1:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        if n<3:
            return 0
        index = 1
        max_len = 0 
        while(index<n-1):
            if(arr[index]>arr[index-1] and arr[index]>arr[index+1]):
                m_len = 3
                #iterate over upward mountain
                slope_index = index-1
                while(slope_index>0):
                    if(arr[slope_index]>arr[slope_index-1]):
                        m_len+=1
                    else:
                        break
                    slope_index-=1
                slope_index = index+2
                #iterate over downward mountain
                while(slope_index<n):
                    if(arr[slope_index-1]>arr[slope_index]):
                        m_len+=1
                    else:
                        break
                    slope_index+=1
                max_len = max(max_len,m_len)
                index = slope_index
            else:
                index+=1
        return max_len