"""
This is a problem on leetcode.com
https://leetcode.com/problems/divide-two-integers/

Problem statement:-
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, assume that your function returns 231 − 1 when the division result overflows.

 

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.
Example 3:

Input: dividend = 0, divisor = 1
Output: 0
Example 4:

Input: dividend = 1, divisor = 1
Output: 1f

Solution1 
p- dividend, q- divisor
Subtracting divisor from the dividend until it becomes less than the divisor
Time complexity- O(p)
Space compexity- O(1)

Solution2
Bit manipulation 
https://www.geeksforgeeks.org/divide-two-integers-without-using-multiplication-division-mod-operator/
"""
from typing import List
import math
class Solution:
    minlimit = -int(math.pow(2,31))
    maxlimit = int(math.pow(2,31))-1
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1
        if( (dividend>0 and divisor<0) or (dividend<0 and divisor>0)):
            sign = -1
        dividend = abs(dividend)# TODO
        divisor = abs(divisor)# TODO
        quot = None
        if(dividend<divisor):
            return 0
        elif(dividend==divisor):
            return sign
        elif(divisor==1):
            quot = sign*dividend
        elif(divisor==2):
            quot = dividend>>1
        else:
            quot = 0
            while(dividend>divisor):
                dividend-=divisor
                quot+=1
            quot = sign*quot
        quot = Solution.maxlimit if quot >Solution.maxlimit else quot
        quot = Solution.minlimit if quot <Solution.minlimit else quot
        return quot


if __name__ == '__main__':
    sol = Solution()
    #Simple cases
    assert sol.divide(10, 3) == 3
    assert sol.divide(11, 3) == 3
    assert sol.divide(-10, 3) == -3
    assert sol.divide(11, -3) == -3
    assert sol.divide(2, -2) == -1
    assert sol.divide(2, 2) == 1
    #Edge cases   
    max_ = int(math.pow(2,31))
    assert sol.divide(max_, 1) == max_-1
    assert sol.divide(max_, -1) == -max_
    assert sol.divide(-max_-1, 1) == -max_
    assert sol.divide(-max_, -1) == max_-1
    print("B-)")


