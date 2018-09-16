#
# [77] Combinations
#
# https://leetcode.com/problems/combinations/description/
#
# algorithms
# Medium (42.79%)
# Total Accepted:    161.1K
# Total Submissions: 371.5K
# Testcase Example:  '4\n2'
#
# Given two integers n and k, return all possible combinations of k numbers out
# of 1 ... n.
# 
# Example:
# 
# 
# Input: n = 4, k = 2
# Output:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
# 
# 
#
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        if k > n:
            return []
        
        candidates = range(1, n+1)
        return self.helper(candidates, k)

    def helper(self, ls, k):
        if k == 1:
            return [[item] for item in ls]
        else:
            ret_ls = []
            for i in range(len(ls)):
                head = ls[i]
                new_candidates = ls[i+1:]
                next_ls = self.helper(new_candidates, k-1)
                for item in next_ls:
                    ret_ls.append([head] + item)
            return ret_ls
        
