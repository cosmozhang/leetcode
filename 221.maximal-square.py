#
# [221] Maximal Square
#
# https://leetcode.com/problems/maximal-square/description/
#
# algorithms
# Medium (31.44%)
# Total Accepted:    106.7K
# Total Submissions: 339.2K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# Given a 2D binary matrix filled with 0's and 1's, find the largest square
# containing only 1's and return its area.
# 
# Example:
# 
# 
# Input: 
# 
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# 
# Output: 4
# 
#
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) < 1 or len(matrix[0]) < 1:
            return 0
        
        m, n = len(matrix), len(matrix[0])

        res_mat = [[0 for _ in range(n)] for _ in range(m)]


        largest = 0
        for i in range(m):
            if matrix[i][0] == '1':
                res_mat[i][0] = 1
                largest = 1

        for j in range(n):
            if matrix[0][j] == '1':
                res_mat[0][j] = 1
                largest = 1


        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    res_mat[i][j] = min(res_mat[i-1][j-1], res_mat[i][j-1], res_mat[i-1][j])+1
                    if res_mat[i][j]**2 > largest:
                        largest = res_mat[i][j] **2
        return largest

