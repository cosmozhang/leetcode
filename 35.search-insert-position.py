#
# [35] Search Insert Position
#
# https://leetcode.com/problems/search-insert-position/description/
#
# algorithms
# Easy (39.94%)
# Total Accepted:    309.7K
# Total Submissions: 775.4K
# Testcase Example:  '[1,3,5,6]\n5'
#
# Given a sorted array and a target value, return the index if the target is
# found. If not, return the index where it would be if it were inserted in
# order.
# 
# You may assume no duplicates in the array.
# 
# Example 1:
# 
# 
# Input: [1,3,5,6], 5
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: [1,3,5,6], 2
# Output: 1
# 
# 
# Example 3:
# 
# 
# Input: [1,3,5,6], 7
# Output: 4
# 
# 
# Example 4:
# 
# 
# Input: [1,3,5,6], 0
# Output: 0
# 
# 
#
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        '''
        for i, v in enumerate(nums):
            if target <= nums[i]:
                return i
        return i+1
        '''

        l = 0
        r = len(nums)-1

        while l <= r:
            m = (l+r)/2
            if nums[m] == target or (m==0 and nums[m]>target):
                return m
            elif m == len(nums) - 1:
                return m+1
            elif nums[m]<target and nums[m+1]>target:
                return m+1
            elif nums[m] < target:
                l = m+1
            elif nums[m] > target:
                r = m
