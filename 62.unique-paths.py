#
# [62] Unique Paths
#
# https://leetcode.com/problems/unique-paths/description/
#
# algorithms
# Medium (43.90%)
# Total Accepted:    217.1K
# Total Submissions: 490.5K
# Testcase Example:  '3\n2'
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
# the diagram below).
# 
# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in
# the diagram below).
# 
# How many possible unique paths are there?
# 
# 
# Above is a 7 x 3 grid. How many possible unique paths are there?
# 
# Note: m and n will be at most 100.
# 
# Example 1:
# 
# 
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the
# bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right
# 
# 
# Example 2:
# 
# 
# Input: m = 7, n = 3
# Output: 28
# 
#
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0:
            return 0
        
        if m == 1 or n == 1:
            return 1

        mat = [[None for j in range(n)] for i in range(m)]
        for i in range(m):
            mat[i][0] = 1

        for j in range(n):
            mat[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                mat[i][j] = mat[i-1][j] + mat[i][j-1]

        return mat[m-1][n-1]
            
