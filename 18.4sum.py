#coding: --utf8--
# [18] 4Sum
#
# https://leetcode.com/problems/4sum/description/
#
# algorithms
# Medium (28.05%)
# Total Accepted:    171.7K
# Total Submissions: 611.2K
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# Given an array nums of n integers and an integer target, are there elements
# a, b, c, and d in nums such that a + b + c + d = target? Find all unique
# quadruplets in the array which gives the sum of target.
# 
# Note:
# 
# The solution set must not contain duplicate quadruplets.
# 
# Example:
# 
# 
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
# 
# A solution set is:
# [
# ⁠ [-1,  0, 0, 1],
# ⁠ [-2, -1, 1, 2],
# ⁠ [-2,  0, 0, 2]
# ]
# 
# 
#
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        else:
            nums.sort()
            res_ls = self.k_sum(nums, target, 4)
            return res_ls
    
    def k_sum(self, nums, target, k):
        res_ls = []
        if k == 2:
            l = 0
            r = len(nums) - 1
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    res_ls.append([nums[l], nums[r]])
                    while l+1 < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r-1 and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif s > target:
                    r -= 1
                elif s < target:
                    l += 1
            return res_ls
        elif k > 2:
            for i in range(len(nums)-k+1):
                s1 = nums[i]
                if i > 0 and nums[i-1] == s1:
                    continue
                rem_ls = self.k_sum(nums[i+1:], target-s1, k-1)
                for j in range(len(rem_ls)):
                    rem_ls[j].append(s1)
                res_ls.extend(rem_ls)
            return res_ls
                
            
# s = Solution()
# print s.fourSum([1,0,-1,0,-2,2], 0)
