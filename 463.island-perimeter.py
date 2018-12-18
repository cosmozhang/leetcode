#
# [463] Island Perimeter
#
# https://leetcode.com/problems/island-perimeter/description/
#
# algorithms
# Easy (59.00%)
# Total Accepted:    106.1K
# Total Submissions: 179.8K
# Testcase Example:  '[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]'
#
# You are given a map in form of a two-dimensional integer grid where 1
# represents land and 0 represents water.
# 
# Grid cells are connected horizontally/vertically (not diagonally). The grid
# is completely surrounded by water, and there is exactly one island (i.e., one
# or more connected land cells).
# 
# The island doesn't have "lakes" (water inside that isn't connected to the
# water around the island). One cell is a square with side length 1. The grid
# is rectangular, width and height don't exceed 100. Determine the perimeter of
# the island.
# 
# 
# 
# Example:
# 
# 
# Input:
# [[0,1,0,0],
# ⁠[1,1,1,0],
# ⁠[0,1,0,0],
# ⁠[1,1,0,0]]
# 
# Output: 16
# 
# Explanation: The perimeter is the 16 yellow stripes in the image below:
# 
# 
# 
# 
#
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        '''
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return self.helper(grid, m, n, i, j)
        '''


        m, n = len(grid), len(grid[0])
        if m == 0 or n == 0:
            return 0
        
        s = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    s += self.cal_tile_pre(i, j, grid, m, n)
        return s

    def cal_tile_pre(self, i, j, grid, m, n):
        dirs = [(0,1), (1, 0), (0,-1), (-1,0)]
        ts = 0
        for xp, yp in dirs:
            ni, nj = i+xp, j+yp
            if ni > m-1 or ni < 0 or nj > n-1 or nj < 0 or grid[ni][nj] == 0:
              ts += 1
        return ts
        
        
    '''
    def helper(self, grid, m, n, i, j):

        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
            return 1
        elif grid[i][j] == 'X':
            return 0
        else:
            grid[i][j] = 'X'
            c = 0
            c += self.helper(grid, m, n, i+1, j)
            c += self.helper(grid, m, n, i-1, j)
            c += self.helper(grid, m, n, i, j+1)
            c += self.helper(grid, m, n, i, j-1)

            return c
    '''
