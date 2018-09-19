#
# [81] Search in Rotated Sorted Array II
#
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
#
# algorithms
# Medium (32.53%)
# Total Accepted:    135.3K
# Total Submissions: 416.7K
# Testcase Example:  '[2,5,6,0,0,1,2]\n0'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
# 
# You are given a target value to search. If found in the array return true,
# otherwise return false.
# 
# Example 1:
# 
# 
# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false
# 
# Follow up:
# 
# 
# This is a follow up problem to Search in Rotated Sorted Array, where nums may
# contain duplicates.
# Would this affect the run-time complexity? How and why?
# 
# 
#
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        
        l = 0
        r = len(nums)-1
        while l <= r:
            m = (l+r)/2
            if nums[m] == target:
                return True
            
            if nums[m] > nums[r]:
                if (nums[m] > target and nums[l] <= target):
                    r = m - 1
                else:
                    l = m + 1
            elif nums[m] < nums[r]:
                if (nums[m] < target and nums[r] >= target):
                    l = m + 1
                else:
                    r = m - 1
            else:
                r -= 1

        return False
