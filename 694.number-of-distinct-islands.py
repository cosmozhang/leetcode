#
# [694] Number of Distinct Islands
#
# https://leetcode.com/problems/number-of-distinct-islands/description/
#
# algorithms
# Medium (47.50%)
# Total Accepted:    15.1K
# Total Submissions: 31.8K
# Testcase Example:  '[[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]'
#
# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's
# (representing land) connected 4-directionally (horizontal or vertical.)  You
# may assume all four edges of the grid are surrounded by water.
# 
# Count the number of distinct islands.  An island is considered to be the same
# as another if and only if one island can be translated (and not rotated or
# reflected) to equal the other.
# 
# Example 1:
# 
# 11000
# 11000
# 00011
# 00011
# 
# Given the above grid map, return 1.
# 
# 
# Example 2:
# 11011
# 10000
# 00001
# 11011
# Given the above grid map, return 3.
# Notice that:
# 
# 11
# 1
# 
# and
# 
# ⁠1
# 11
# 
# are considered different island shapes, because we do not consider reflection
# / rotation.
# 
# 
# Note:
# The length of each dimension in the given grid does not exceed 50.
# 
#
class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid)<1 or len(grid[0])<1:
            return 0
        
        m = len(grid)
        n = len(grid[0])
        island_set = set()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    k =self.normalize(self.find_island_shape(grid, m, n, i, j))    
                    island_set.add(tuple(k))
                    
        return len(island_set)

    
    def find_island_shape(self, grid, m, n, i, j):
        
        if i<0 or i>=m or j<0 or j>=n or grid[i][j] == 'X' or grid[i][j] == 0:
            return []
        else:
            res_ls = [(i, j)]
            grid[i][j] = 'X'
            res_ls += self.find_island_shape(grid, m, n, i+1, j)
            res_ls += self.find_island_shape(grid, m, n, i-1, j)
            res_ls += self.find_island_shape(grid, m, n, i, j+1)
            res_ls += self.find_island_shape(grid, m, n, i, j-1)
            return res_ls
        
    def normalize(self, ts):

        min_x = min([t[0] for t in ts])
        min_y = min([t[1] for t in ts])

        return [(t[0]-min_x, t[1]-min_y) for t in ts]
            

        
                    
