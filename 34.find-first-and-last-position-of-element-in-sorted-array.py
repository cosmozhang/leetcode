#
# [34] Find First and Last Position of Element in Sorted Array
#
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (31.88%)
# Total Accepted:    215.3K
# Total Submissions: 673.9K
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# Given an array of integers nums sorted in ascending order, find the starting
# and ending position of a given target value.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# If the target is not found in the array, return [-1, -1].
# 
# Example 1:
# 
# 
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# 
# Example 2:
# 
# 
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# 
#
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        '''
        if len(nums)<1:
            return [-1,-1]
        if target > nums[-1] or target < nums[0]:
            return [-1, -1]
        # find left
        l, r = 0, len(nums)-1
        while l < r:
            m = (l+r)/2
            if nums[m] < target:
                l = m+1
            elif nums[m] >= target:
                r = m
        left_pos = l
        # find right
        l, r = left_pos, len(nums)-1
        while l < r:
            m = (l+r)/2
            if l+1 == r:
                break
            if nums[m] <= target:
                l = m
            elif nums[m] > target:
                r = m-1
        if nums[r] == target:
            right_pos = r
        else:
            right_pos = r-1
        if nums[left_pos] != target:
            left_pos, right_pos =-1, -1
        return [left_pos, right_pos]
        '''

        s, e = -1, -1

        l, r = 0, len(nums)-1

        while l < r:
            m = (l+r) >> 1
            if nums[m] > target:
                r = m-1
            elif nums[m] < target:
                l = m+1
            else:
                r = m
        if len(nums) > 0 and nums[r] == target:
            s = r

        l, r = 0, len(nums)-1
        while l < r:
            m = (l+r) >> 1
            if nums[m] > target:
                r = m-1
            elif nums[m] < target:
                l = m+1
            else:
                if l + 1 != r:
                    l = m
                else:
                    if target == nums[l+1]:
                        l+=1
                        break
                    else:
                        break
        if len(nums) >0 and nums[l] == target:
            e = l

        return [s, e]
                    
                    
        
