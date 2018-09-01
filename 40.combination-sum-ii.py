#
# [40] Combination Sum II
#
# https://leetcode.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (37.22%)
# Total Accepted:    168.9K
# Total Submissions: 450.1K
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# Given a collection of candidate numbers (candidates) and a target number
# (target), find all unique combinations in candidates where the candidate
# numbers sums to target.
# 
# Each number in candidates may only be used once in the combination.
# 
# Note:
# 
# 
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# 
# 
# Example 1:
# 
# 
# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
# ⁠ [1, 7],
# ⁠ [1, 2, 5],
# ⁠ [2, 6],
# ⁠ [1, 1, 6]
# ]
# 
# 
# Example 2:
# 
# 
# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
# [1,2,2],
# [5]
# ]
# 
# 
#
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        if candidates == [] or target < candidates[0]:
            return []
        ret_ls = []
        for inv_i in range(len(candidates)-1, -1, -1):
            if inv_i != len(candidates)-1 and candidates[inv_i] == candidates[inv_i+1]:
                continue
            c = candidates[inv_i]
            if c == target:
                ret_ls.append([c])
            elif c < target:
                if inv_i > 0:
                    cand_ls = self.combinationSum2(candidates[:inv_i], target-c)
                    if cand_ls != []:
                        ret_ls.extend([res_ls+[c] for res_ls in cand_ls])
            else:
                continue

        return ret_ls
