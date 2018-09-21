#
# [90] Subsets II
#
# https://leetcode.com/problems/subsets-ii/description/
#
# algorithms
# Medium (39.31%)
# Total Accepted:    165.1K
# Total Submissions: 415.6K
# Testcase Example:  '[1,2,2]'
#
# Given a collection of integers that might contain duplicates, nums, return
# all possible subsets (the power set).
# 
# Note: The solution set must not contain duplicate subsets.
# 
# Example:
# 
# 
# Input: [1,2,2]
# Output:
# [
# ⁠ [2],
# ⁠ [1],
# ⁠ [1,2,2],
# ⁠ [2,2],
# ⁠ [1,2],
# ⁠ []
# ]
# 
#
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()

        ret_ls = [[]]
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                temp_ls = [[nums[i]] + item for item in ret_ls[-c:]]
                ret_ls = ret_ls + temp_ls

            else:
                temp_ls = [[nums[i]] + item for item in ret_ls]
                c = len(temp_ls)
                ret_ls = ret_ls + temp_ls
            
        return ret_ls

