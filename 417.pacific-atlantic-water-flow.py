#
# [417] Pacific Atlantic Water Flow
#
# https://leetcode.com/problems/pacific-atlantic-water-flow/description/
#
# algorithms
# Medium (35.68%)
# Total Accepted:    34.7K
# Total Submissions: 97.3K
# Testcase Example:  '[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]'
#
# Given an m x n matrix of non-negative integers representing the height of
# each unit cell in a continent, the "Pacific ocean" touches the left and top
# edges of the matrix and the "Atlantic ocean" touches the right and bottom
# edges.
# 
# Water can only flow in four directions (up, down, left, or right) from a cell
# to another one with height equal or lower.
# 
# Find the list of grid coordinates where water can flow to both the Pacific
# and Atlantic ocean.
# 
# Note:
# 
# The order of returned grid coordinates does not matter.
# Both m and n are less than 150.
# 
# 
# Example:
# 
# Given the following 5x5 matrix:
# 
# ⁠ Pacific ~   ~   ~   ~   ~ 
# ⁠      ~  1   2   2   3  (5) *
# ⁠      ~  3   2   3  (4) (4) *
# ⁠      ~  2   4  (5)  3   1  *
# ⁠      ~ (6) (7)  1   4   5  *
# ⁠      ~ (5)  1   1   2   4  *
# ⁠         *   *   *   *   * Atlantic
# 
# Return:
# 
# [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with
# parentheses in above matrix).
# 
# 
#
class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        
        m, n = len(matrix), len(matrix[0])

        recmat = [[[False, False] for _ in range(n)] for _ in range(m)]
        
        ret_ls = []
        for i in range(m):
            self.findFlowToA(i, n-1, m, n, matrix, recmat)
            self.findFlowToP(i, 0, m, n, matrix, recmat)
            
        for j in range(n):
            self.findFlowToA(m-1, j, m, n, matrix, recmat)
            self.findFlowToP(0, j, m, n, matrix, recmat)

        for i in range(m):
            for j in range(n):
                if recmat[i][j][0] and recmat[i][j][1]:
                    ret_ls.append([i, j])

        return ret_ls

    def findFlowToA(self, i, j, m, n, matrix, recmat):
        recmat[i][j][1] = True
        
        dirs = [[1,0], [0,1], [-1,0], [0,-1]]
        for idx, (xp, yp) in enumerate(dirs):
            newi = i+xp
            newj = j+yp

            if newi > -1 and newi < m and newj > -1 and newj < n and matrix[newi][newj] >= matrix[i][j] and not recmat[newi][newj][1]:
                tmp = matrix[i][j]
                matrix[i][j] = float('-inf')
                self.findFlowToA(newi, newj, m, n, matrix, recmat)
                matrix[i][j] = tmp

            
    def findFlowToP(self, i, j, m, n, matrix, recmat):
        recmat[i][j][0] = True
        
        dirs = [[1,0], [0,1], [-1,0], [0,-1]]
        for idx, (xp, yp) in enumerate(dirs):
            newi = i+xp
            newj = j+yp

            if newi > -1 and newi < m and newj > -1 and newj < n and matrix[newi][newj] >= matrix[i][j] and not recmat[newi][newj][0]:
                tmp = matrix[i][j]
                matrix[i][j] = float('-inf')
                self.findFlowToP(newi, newj, m, n, matrix, recmat)
                matrix[i][j] = tmp

        

                
