# coding: --utf-8--
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (32.01%)
# Total Accepted:    291.7K
# Total Submissions: 910.5K
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
#
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
#
# You are given a target value to search. If found in the array return its
# index, otherwise return -1.
#
# You may assume no duplicate exists in the array.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# Example 1:
#
#
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
#
#
# Example 2:
#
#
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
#
# First determine which side the middle point is located, then determine which side the target is located.
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        '''
        l = 0
        r = len(nums) - 1
        ret = -1
        while l <= r:
            m = (l+r)/2
            if nums[m] == target:
                ret = m
                break
            if nums[m] >= nums[l]:
                if nums[m] > target and target >= nums[l]:
                    r = m-1
                else:
                    l = m+1
            elif nums[m] <= nums[r]:
                if nums[m] < target and target <= nums[r]:
                    l = m+1
                else:
                    r = m-1
        return ret
        '''

        l, r = 0, len(nums)-1

        while l <= r:
            m = (l+r) >> 1
            if nums[m] == target:
                return m
            if nums[m] >= nums[l]:
                if target >= nums[l] and target < nums[m]:
                    r = m-1
                else:
                    l = m+1
            elif nums[m] < nums[l]:
                if target > nums[m] and target <= nums[r]:
                    l = m+1
                else:
                    r = m-1

        return -1

