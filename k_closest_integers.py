"""
This is a problem on leetcode.com
https://leetcode.com/problems/find-k-closest-elements/submissions/

------------------------
Problem statement
------------------------

Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
 

Constraints:

1 <= k <= arr.length
1 <= arr.length <= 104
arr is sorted in ascending order.
-104 <= arr[i], x <= 104

------------------------
Solutions
------------------------
Solution1
First find the index, such that  (Can be done by using bisect_left function from bisect library)
    either arr[index-1]<x<=arr[index]

Use two pointer approach to find k closest integers

"""
from collections import deque
import bisect
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n =len(arr)
        #find the inserting position for k
        left = 0 
        right = n-1
        index = None
        while(right>left):
            mid= int( (left+right)/2)
            if(arr[mid]<x):
                left = mid+1      
            elif(arr[mid]>x):
                right = mid-1
            else:
                index = mid
                #iterate over duplicate elements
                while(index>0 and arr[index-1]==x):
                    index-=1
                    break
                break
        #if not equal
        if not index:
            index = left
            if(index+1<n and arr[index]<x and arr[index+1]>x):
                index+=1
        # index = bisect.bisect_left(arr,x)
            
        
        
        #function to find closest
        def closestInt(val,a,b):
            dist_a = abs(val-a)
            dist_b = abs(val-b)

            if(dist_a<dist_b):
                return a
            elif(dist_a>dist_b):
                return b
            else:
                return a if a<b else b
        closest = deque()
        left = index-1
        right = index
        while(len(closest)<k and left>-1 and right<n):
            if(closestInt(x,arr[left],arr[right])==arr[left]):
                closest.appendleft(arr[left])
                left-=1
            else:
                closest.append(arr[right])
                right+=1
        
        while(len(closest)<k and left>-1):
            closest.appendleft(arr[left])
            left-=1
      
        while(len(closest)<k and right<n):
            closest.append(arr[right])
            right+=1
  
        return closest