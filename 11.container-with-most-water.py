#
# [11] Container With Most Water
#
# https://leetcode.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (37.78%)
# Total Accepted:    223.7K
# Total Submissions: 591.7K
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# Given n non-negative integers a1, a2, ..., an , where each represents a point
# at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
# of line i is at (i, ai) and (i, 0). Find two lines, which together with
# x-axis forms a container, such that the container contains the most water.
# 
# Note: You may not slant the container and n is at least 2.
# 
# 
# 
# 
# 
# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In
# this case, the max area of water (blue section) the container can contain is
# 49. 
# 
# 
# 
# Example:
# 
# 
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49
# 
#
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        s_id = 0
        e_id = len(height) - 1
        max_a = 0
        while s_id < e_id:
            cur_a = (e_id-s_id) * min(height[s_id], height[e_id])
            if cur_a > max_a:
                max_a = cur_a
            if height[s_id] > height[e_id]:
                e_id -= 1
            else:
                s_id += 1
        return max_a
