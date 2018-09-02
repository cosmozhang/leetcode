#
# [47] Permutations II
#
# https://leetcode.com/problems/permutations-ii/description/
#
# algorithms
# Medium (36.26%)
# Total Accepted:    183.5K
# Total Submissions: 502.2K
# Testcase Example:  '[1,1,2]'
#
# Given a collection of numbers that might contain duplicates, return all
# possible unique permutations.
# 
# Example:
# 
# 
# Input: [1,1,2]
# Output:
# [
# ⁠ [1,1,2],
# ⁠ [1,2,1],
# ⁠ [2,1,1]
# ]
# 
# 
#
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        if len(nums) < 2:
            return [nums]
        else:
            ret_ls =[]
            for i in range(len(nums)):
                if i>0 and nums[i] == nums[i-1]:
                    continue
                prev_ls = self.permuteUnique(nums[:i]+nums[i+1:])
                for per in prev_ls:
                    ret_ls.append([nums[i]]+per)
            return ret_ls
