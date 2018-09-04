#
# [54] Spiral Matrix
#
# https://leetcode.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (27.90%)
# Total Accepted:    165.1K
# Total Submissions: 588.3K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a matrix of m x n elements (m rows, n columns), return all elements of
# the matrix in spiral order.
# 
# Example 1:
# 
# 
# Input:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# 
# 
# Example 2:
# 
# Input:
# [
# ⁠ [1, 2, 3, 4],
# ⁠ [5, 6, 7, 8],
# ⁠ [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
# 
#
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []
        
        ret_ls = []

        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = n-1
        up = 0
        down = m-1

        while True:

            for i in range(left, right+1):
                ret_ls.append(matrix[up][i])
            up += 1
            if up > down:
                break

            for i in range(up, down+1):
                ret_ls.append(matrix[i][right])
            right -= 1
            if left > right:
                break
                
            for i in range(right, left-1, -1):
                ret_ls.append(matrix[down][i])
            down -= 1
            if up > down:
                break
                
            for i in range(down, up-1, -1):
                ret_ls.append(matrix[i][left])
            left += 1
            if left > right:
                break
        return ret_ls
