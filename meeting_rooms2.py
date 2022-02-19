"""
This is a problem on leetcode.com. It requires premium access
https://leetcode.com/problems/meeting-rooms-ii/
Same problem on interviewbit
https://www.interviewbit.com/problems/meeting-rooms/
------------------------
Problem statement
------------------------
Given an 2D integer array A of size N x 2 denoting time intervals of different meetings.
Where:

A[i][0] = start time of the ith meeting.
A[i][1] = end time of the ith meeting.
Find the minimum number of conference rooms required so that all meetings can be done.


--------------
Solution1
--------------
Step1- 
First sort the time intervals in increasing order of start time. Iterate over intervals 

Time complexity O(nlgn) Space complexity O(1)
Step2- 
For each interval
   pick the meeting room which is available earliest i.e the one with minimum end time of last meeting in the room
   If start time is greater or equal to this end time, change the end time of this room
   else: get new meeting room
Time complexity  Sum(lg(i)) =>O(nlgn) 
Space complexity O(n)
    
"""
import heapq
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        time_heap = []
        for interval in A:
            start, end = interval[0], interval[1]
            if time_heap and time_heap[0]<=start:
                heapq.heapreplace(time_heap, end)
            else:
                heapq.heappush(time_heap, end)
        return len(time_heap)