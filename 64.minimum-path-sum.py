#
# [64] Minimum Path Sum
#
# https://leetcode.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (42.24%)
# Total Accepted:    172.3K
# Total Submissions: 402.8K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# Given a m x n grid filled with non-negative numbers, find a path from top
# left to bottom right which minimizes the sum of all numbers along its path.
# 
# Note: You can only move either down or right at any point in time.
# 
# Example:
# 
# 
# Input:
# [
# [1,3,1],
# ⁠ [1,5,1],
# ⁠ [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.
# 
# 
#
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])

        v_mat = [[0 for j in range(n)] for i in range(m)]

        v_mat[0][0] = grid[0][0]
        for i in range(1, m):
            v_mat[i][0] = v_mat[i-1][0]+grid[i][0]

        for j in range(1, n):
            v_mat[0][j] = v_mat[0][j-1]+grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                if v_mat[i-1][j] < v_mat[i][j-1]:
                    path_v = v_mat[i-1][j]
                else:
                    path_v = v_mat[i][j-1]
                v_mat[i][j] = path_v+grid[i][j]
                
        return v_mat[m-1][n-1]
