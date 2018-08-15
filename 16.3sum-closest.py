#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest/description/
#
# algorithms
# Medium (32.28%)
# Total Accepted:    192.7K
# Total Submissions: 596.3K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# Given an array nums of n integers and an integer target, find three integers
# in nums such that the sum is closest to target. Return the sum of the three
# integers. You may assume that each input would have exactly one solution.
# 
# Example:
# 
# 
# Given array nums = [-1, 2, 1, -4], and target = 1.
# 
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# 
# 
#
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        min_dis = float("Inf")
        nums.sort()
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            while l < r:
                s = nums[l] + nums[r] + nums[i]
                new_dis = abs(s-target)
                if new_dis < min_dis:
                    min_dis = new_dis
                    min_s = s
                if s - target > 0:
                    r -= 1
                elif s - target < 0:
                    l += 1
                else:
                    min_s = target
                    break
        return min_s
