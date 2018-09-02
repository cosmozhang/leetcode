#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (49.14%)
# Total Accepted:    269.9K
# Total Submissions: 544.7K
# Testcase Example:  '[1,2,3]'
#
# Given a collection of distinct integers, return all possible permutations.
# 
# Example:
# 
# 
# Input: [1,2,3]
# Output:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
# 
#
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <2:
            return [nums]
        
        if len(nums) == 2:
            return [[nums[0], nums[1]], [nums[1], nums[0]]]
        else:
            ret_ls = []
            next_ls = self.permute(nums[1:])
            for per in next_ls:
                ret_ls.append([nums[0]] + per)
                ret_ls.append(per + [nums[0]])
                for i in range(1, len(per)):
                    ret_ls.append(per[:i] + [nums[0]] + per[i:])
            return ret_ls
            
