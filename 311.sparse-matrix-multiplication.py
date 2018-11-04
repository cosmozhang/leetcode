#
# [311] Sparse Matrix Multiplication
#
# https://leetcode.com/problems/sparse-matrix-multiplication/description/
#
# algorithms
# Medium (54.12%)
# Total Accepted:    55.3K
# Total Submissions: 102.2K
# Testcase Example:  '[[1,0,0],[-1,0,3]]\n[[7,0,0],[0,0,0],[0,0,1]]'
#
# Given two sparse matrices A and B, return the result of AB.
# 
# You may assume that A's column number is equal to B's row number.
# 
# Example:
# 
# 
# Input:
# 
# A = [
# ⁠ [ 1, 0, 0],
# ⁠ [-1, 0, 3]
# ]
# 
# B = [
# ⁠ [ 7, 0, 0 ],
# ⁠ [ 0, 0, 0 ],
# ⁠ [ 0, 0, 1 ]
# ]
# 
# Output:
# 
# ⁠    |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
# AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
# ⁠                 | 0 0 1 |
# 
# 
#
class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        
        I, K = len(A), len(A[0])

        J = len(B[0])

        
        n_matrix = [[0 for j in range(J)] for i in range(I)]

        '''
        A_dic = {}
        for i in range(I):
            row_set = set()
            for k in range(K):
                if A[i][k] != 0:
                    row_set.add(k)
            A_dic[i] = row_set


        B_dic = {}
        for j in range(J):
            col_set = set()
            for k in range(K):
                if B[k][j] != 0:
                    col_set.add(k)
            B_dic[j] = col_set
        '''
        
        for i in range(I):
            for j in range(J):
                if any(A[i]):
                    for k in range(K):
                        n_matrix[i][j] += A[i][k]*B[k][j]
        
        return n_matrix
