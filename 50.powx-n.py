#
# [50] Pow(x, n)
#
# https://leetcode.com/problems/powx-n/description/
#
# algorithms
# Medium (26.40%)
# Total Accepted:    237.5K
# Total Submissions: 896.4K
# Testcase Example:  '2.00000\n10'
#
# Implement pow(x, n), which calculates x raised to the power n (xn).
#
# Example 1:
#
#
# Input: 2.00000, 10
# Output: 1024.00000
#
#
# Example 2:
#
#
# Input: 2.10000, 3
# Output: 9.26100
#
#
# Example 3:
#
#
# Input: 2.00000, -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25
#
#
# Note:
#
#
# -100.0 < x < 100.0
# n is a 32-bit signed integer, within the range [−231, 231 − 1]
#
#
#


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        '''
        if n == 0:
            return 1
        elif n == 1:
            return x
        else:
            if n < 0:
                return 1.0/self.myPow(x, -n)
            else:
                halfx = self.myPow(x, n/2)
                if n%2 == 0:
                    return halfx*halfx
                else:
                    return halfx*halfx*x
        '''

        if x == 0:
            return 0

        if n == 0:
            return 1 
        elif n == 1:
            return x
        elif n > 0:
            h = self.myPow(x, n/2)
            if n%2 == 0:
                ret = h*h
            else:
                ret = h*h*x
            return ret
        else:
            n = -n
            h = self.myPow(x, n/2)
            if n%2 == 0:
                ret = h*h
            else:
                ret = h*h*x
            return 1/ret
