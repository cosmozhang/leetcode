#
# [280] Wiggle Sort
#
# https://leetcode.com/problems/wiggle-sort/description/
#
# algorithms
# Medium (59.67%)
# Total Accepted:    54.6K
# Total Submissions: 91.4K
# Testcase Example:  '[3,5,2,1,6,4]'
#
# Given an unsorted array nums, reorder it in-place such that nums[0] <=
# nums[1] >= nums[2] <= nums[3]....
# 
# Example:
# 
# 
# Input: nums = [3,5,2,1,6,4]
# Output: One possible answer is [3,5,1,6,2,4]
# 
#
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        '''
        nums.sort()
        n = len(nums)

        if n%2==0:
            #even
            v = n/2
        else:
            #odd
            v = n/2+1
        for s, e in zip(range(1, n, 2), range(v, n)):
            t = nums[e]
            nums[s+1:e+1] = nums[s:e]
            nums[s] = t
        '''
        n = len(nums)
        for i in range(n):
            if i&1 == 0:
                if i+1 < n:
                    if nums[i] > nums[i+1]:
                        nums[i], nums[i+1] = nums[i+1], nums[i]
            else:
                if i+1 < n:
                    if nums[i] < nums[i+1]:
                        nums[i+1], nums[i] = nums[i], nums[i+1]
        
