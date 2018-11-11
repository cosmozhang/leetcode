#
# [866] Rectangle Overlap
#
# https://leetcode.com/problems/rectangle-overlap/description/
#
# algorithms
# Easy (44.43%)
# Total Accepted:    13.3K
# Total Submissions: 30K
# Testcase Example:  '[0,0,2,2]\n[1,1,3,3]'
#
# A rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) are the
# coordinates of its bottom-left corner, and (x2, y2) are the coordinates of
# its top-right corner.
# 
# Two rectangles overlap if the area of their intersection is positive.  To be
# clear, two rectangles that only touch at the corner or edges do not overlap.
# 
# Given two (axis-aligned) rectangles, return whether they overlap.
# 
# Example 1:
# 
# 
# Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
# Output: false
# 
# 
# Notes:
# 
# 
# Both rectangles rec1 and rec2 are lists of 4 integers.
# All coordinates in rectangles will be between -10^9 and 10^9.
# 
# 
#
class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        
        x1_1, y1_1, x1_2, y1_2 = rec1[0], rec1[1], rec1[2], rec1[3]
        x2_1, y2_1, x2_2, y2_2 = rec2[0], rec2[1], rec2[2], rec2[3]

        one = y2_1 < y1_2 and x1_1 < x2_2 and x2_1 < x1_2 and y1_1 < y2_2
        
        two = x2_1 < x1_2 and y2_1 < y1_2 and x1_1 < x2_2 and y1_1 < y2_2
        
        three = x2_1 < x1_2 and y1_1 < y2_2 and x1_1 < x2_2 and y2_1 < y1_2
        
        four = x1_1 < x2_2 and y1_1 < y2_2 and x2_1 < x1_2 and y2_1 < y1_2

        return one or two or three or four

        
