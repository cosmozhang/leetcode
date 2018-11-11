#
# [231] Power of Two
#
# https://leetcode.com/problems/power-of-two/description/
#
# algorithms
# Easy (41.21%)
# Total Accepted:    197.2K
# Total Submissions: 478.5K
# Testcase Example:  '1'
#
# Given an integer, write a function to determine if it is a power of two.
# 
# Example 1:
# 
# 
# Input: 1
# Output: true 
# Explanation: 20 = 1
# 
# 
# Example 2:
# 
# 
# Input: 16
# Output: true
# Explanation: 24 = 16
# 
# Example 3:
# 
# 
# Input: 218
# Output: false
# 
#
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        nn = bin(n)
        if len(nn) == 3:
            if nn[2] == '1':
                return True
            else:
                return False
        else:
            return sum([int(k) for k in list(nn[3:])]) == 0
