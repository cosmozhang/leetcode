#
# [63] Unique Paths II
#
# https://leetcode.com/problems/unique-paths-ii/description/
#
# algorithms
# Medium (32.49%)
# Total Accepted:    154K
# Total Submissions: 472.6K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
# the diagram below).
# 
# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in
# the diagram below).
# 
# Now consider if some obstacles are added to the grids. How many unique paths
# would there be?
# 
# 
# 
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
# 
# Note: m and n will be at most 100.
# 
# Example 1:
# 
# 
# Input:
# [
# [0,0,0],
# [0,1,0],
# [0,0,0]
# ]
# Output: 2
# Explanation:
# There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
# 
# 
#
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:
            return 0
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[m-1][n-1] == 1:
            return 0

        cal_mat = [[0 for i in range(n)] for j in range(m)]

        print cal_mat

        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            cal_mat[i][0] = 1

        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            cal_mat[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i-1][j] == 1:
                    from_top = 0
                else:
                    from_top = cal_mat[i-1][j]
                if obstacleGrid[i][j-1] == 1:
                    from_left = 0
                else:
                    from_left = cal_mat[i][j-1]

                cal_mat[i][j] = from_top + from_left
                
        return cal_mat[m-1][n-1]
                
                    
