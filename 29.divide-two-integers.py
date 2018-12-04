#
# [29] Divide Two Integers
#
# https://leetcode.com/problems/divide-two-integers/description/
#
# algorithms
# Medium (15.70%)
# Total Accepted:    146.4K
# Total Submissions: 931.6K
# Testcase Example:  '10\n3'
#
# Given two integers dividend and divisor, divide two integers without using
# multiplication, division and mod operator.
#
# Return the quotient after dividing dividend by divisor.
#
# The integer division should truncate toward zero.
#
# Example 1:
#
#
# Input: dividend = 10, divisor = 3
# Output: 3
#
# Example 2:
#
#
# Input: dividend = 7, divisor = -3
# Output: -2
#
# Note:
#
#
# Both dividend and divisor will be 32-bit signed integers.
# The divisor will never be 0.
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of
# this problem, assume that your function returns 231 − 1 when the division
# result overflows.
#
#
#
# plus as a way to do mulplication
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        '''
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        if dividend == 0:
            return 0

        if dividend < 0:
            dividend = - dividend
            if divisor < 0:
                divisor = -divisor
                sgn = 1
            elif divisor > 0:
                sgn = -1
        elif dividend > 0:
            if divisor < 0:
                divisor = -divisor
                sgn = -1
            elif divisor >0:
                sgn = 1
        res = 0
        while divisor <= dividend:
            s = divisor
            t = 1
            while (s + s) <= dividend:
                s += s
                t += t
            dividend -= s
            res += t
        if sgn == 1:
            return res
        elif sgn == -1:
            return -res
        '''

        if dividend == -2**31 and divisor == -1:
            return 2**31-1

        if abs(dividend) < abs(divisor):
            return 0

        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            sign = 1

        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            sign = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
            
        t = 0
        ndivisor = divisor
        while ndivisor <= dividend:
            s = 1
            while ndivisor*2 <= dividend:
                s *= 2
                ndivisor *= 2

            dividend = dividend - ndivisor
            ndivisor = divisor
            t += s

        if sign == -1:
            return -t
        else:
            return t
                
                

                

            
