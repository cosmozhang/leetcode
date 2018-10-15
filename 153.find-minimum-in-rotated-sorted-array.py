# -*- coding:utf-8 -*-
# [153] Find Minimum in Rotated Sorted Array
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
#
# algorithms
# Medium (41.71%)
# Total Accepted:    228.6K
# Total Submissions: 548K
# Testcase Example:  '[3,4,5,1,2]'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
# 
# Find the minimum element.
# 
# You may assume no duplicate exists in the array.
# 
# Example 1:
# 
# 
# Input: [3,4,5,1,2] 
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: [4,5,6,7,0,1,2]
# Output: 0
# 
# 
#
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        l = 0
        r = len(nums)-1

        while True:
            m =(l+r)/2
            if nums[m] > nums[-1]:
                l = m
            else:
                r = m

            if l == r:
                return nums[r]
            elif l+1 == r:
                if nums[l]<nums[r]:
                    return nums[l]
                else:
                    return nums[r]

