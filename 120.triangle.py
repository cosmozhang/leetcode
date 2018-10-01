#
# [120] Triangle
#
# https://leetcode.com/problems/triangle/description/
#
# algorithms
# Medium (36.54%)
# Total Accepted:    149.6K
# Total Submissions: 409.3K
# Testcase Example:  '[[2],[3,4],[6,5,7],[4,1,8,3]]'
#
# Given a triangle, find the minimum path sum from top to bottom. Each step you
# may move to adjacent numbers on the row below.
# 
# For example, given the following triangle
# 
# 
# [
# ⁠    [2],
# ⁠   [3,4],
# ⁠  [6,5,7],
# ⁠ [4,1,8,3]
# ]
# 
# 
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
# 
# Note:
# 
# Bonus point if you are able to do this using only O(n) extra space, where n
# is the total number of rows in the triangle.
# 
#
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        
        triangle.reverse()

        tmp_ls = [i for i in triangle[0]]
        for i in range(len(triangle)-1):
            upper = triangle[i+1]
            for j in range(len(upper)):
                tmp_ls[j] = min(upper[j]+tmp_ls[j], upper[j]+tmp_ls[j+1])

        return tmp_ls[0]
                
            