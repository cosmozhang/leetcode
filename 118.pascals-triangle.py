#
# [118] Pascal's Triangle
#
# https://leetcode.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (42.36%)
# Total Accepted:    199.5K
# Total Submissions: 470.3K
# Testcase Example:  '5'
#
# Given a non-negative integer numRows, generate the first numRows of Pascal's
# triangle.
# 
# 
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it.
# 
# Example:
# 
# 
# Input: 5
# Output:
# [
# ⁠    [1],
# ⁠   [1,1],
# ⁠  [1,2,1],
# ⁠ [1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
# 
# 
#
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
    
        if numRows == 0:
            return []

        ret_ls = []
        for i in range(numRows):
            if i == 0:
                ret_ls.append([1])
            elif i == 1:
                ret_ls.append([1,1])
            else:
                ret_ls.append([1]+[ret_ls[-1][j]+ret_ls[-1][j+1] for j in range(i-1)]+[1])
        return ret_ls
            
