#
# [279] Perfect Squares
#
# https://leetcode.com/problems/perfect-squares/description/
#
# algorithms
# Medium (39.11%)
# Total Accepted:    139.5K
# Total Submissions: 356.5K
# Testcase Example:  '12'
#
# Given a positive integer n, find the least number of perfect square numbers
# (for example, 1, 4, 9, 16, ...) which sum to n.
# 
# Example 1:
# 
# 
# Input: n = 12
# Output: 3 
# Explanation: 12 = 4 + 4 + 4.
# 
# Example 2:
# 
# 
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
#
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [float('inf') for _ in range(n+1)]
        dp[0] = 0

        for i in range(1, n+1):
            j = 0
            while j**2 <= i:
                dp[i] = min(dp[i-j**2]+1, dp[i])
                j += 1
        return dp[n]
