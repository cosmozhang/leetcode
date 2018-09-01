#
# [39] Combination Sum
#
# https://leetcode.com/problems/combination-sum/description/
#
# algorithms
# Medium (42.92%)
# Total Accepted:    246.6K
# Total Submissions: 570.2K
# Testcase Example:  '[2,3,6,7]\n7'
#
# Given a set of candidate numbers (candidates) (without duplicates) and a
# target number (target), find all unique combinations in candidates where the
# candidate numbers sums to target.
# 
# The same repeated number may be chosen from candidates unlimited number of
# times.
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
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
# ⁠ [7],
# ⁠ [2,2,3]
# ]
# 
# 
# Example 2:
# 
# 
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
# [2,2,2,2],
# [2,3,3],
# [3,5]
# ]
# 
# 
#
class Solution(object):
    def combinationSum(self, candidates, target):
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
            mod = target % candidates[inv_i]
            n = target/candidates[inv_i]
            if mod == 0:
                ret_ls.append([candidates[inv_i] for i in range(n)])
            if mod < target and candidates[:inv_i]:
                for j in range(1, n+1):
                    prev_ls = self.combinationSum(candidates[:inv_i], target-j*candidates[inv_i])
                    if prev_ls != []:
                        ret_ls.extend([res_ls+[candidates[inv_i] for i in range(j)] for res_ls in prev_ls])
            elif mod == target:
                continue
        return ret_ls
