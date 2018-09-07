#
# [59] Spiral Matrix II
#
# https://leetcode.com/problems/spiral-matrix-ii/description/
#
# algorithms
# Medium (42.36%)
# Total Accepted:    111.3K
# Total Submissions: 260K
# Testcase Example:  '3'
#
# Given a positive integer n, generate a square matrix filled with elements
# from 1 to n2 in spiral order.
# 
# Example:
# 
# 
# Input: 3
# Output:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 8, 9, 4 ],
# ⁠[ 7, 6, 5 ]
# ]
# 
# 
#
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        top = 0
        bottom = n-1
        left = 0
        right = n-1
        nums = range(1, n**2+1)
        idx = 0
        ret_mat = [[0 for i in range(n)] for i in range(n)]
        while True:
            for j in range(left, right+1):
                ret_mat[top][j] = nums[idx]
                idx += 1
            top += 1
            if top > bottom:
                break

            for j in range(top, bottom+1):
                ret_mat[j][right] = nums[idx]
                idx += 1
            right -= 1
            if right < left:
                break

            for j in range(right, left-1, -1):
                ret_mat[bottom][j] = nums[idx]
                idx += 1
            bottom -=1
            if bottom < top:
                break

            for j in range(bottom, top-1, -1):
                ret_mat[j][left]= nums[idx]
                idx += 1
            left += 1
            if left > right:
                break

        return ret_mat
