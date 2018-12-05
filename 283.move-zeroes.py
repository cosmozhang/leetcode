#
# [283] Move Zeroes
#
# https://leetcode.com/problems/move-zeroes/description/
#
# algorithms
# Easy (52.66%)
# Total Accepted:    368.6K
# Total Submissions: 699.7K
# Testcase Example:  '[0,1,0,3,12]'
#
# Given an array nums, write a function to move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.
# 
# Example:
# 
# 
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# 
# Note:
# 
# 
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
# 
#
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        '''
        l = 0
        r = 1

        while r < len(nums):
            if nums[l] == 0:
                if nums[r] != 0:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r += 1
                else:
                    r += 1
            else:
                l += 1
                r += 1
        '''
        if len(nums) > 1:
            l = 0
            r = 0

            while r < len(nums):
                if nums[l] == 0:
                    if nums[r] != 0:
                        nums[l], nums[r] = nums[r], nums[l]
                        l+=1
                        r+=1
                    else:
                        r+=1
                else:
                    l+=1
                    r+=1
