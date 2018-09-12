#coding: --utf-8--
# [60] Permutation Sequence
#
# https://leetcode.com/problems/permutation-sequence/description/
#
# algorithms
# Medium (30.27%)
# Total Accepted:    112.4K
# Total Submissions: 367.8K
# Testcase Example:  '3\n3'
#
# The set [1,2,3,...,n] contains a total of n! unique permutations.
# 
# By listing and labeling all of the permutations in order, we get the
# following sequence for n = 3:
# 
# 
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# 
# 
# Given n and k, return the kth permutation sequence.
# 
# Note:
# 
# 
# Given n will be between 1 and 9 inclusive.
# Given k will be between 1 and n! inclusive.
# 
# 
# Example 1:
# 
# 
# Input: n = 3, k = 3
# Output: "213"
# 
# 
# Example 2:
# 
# 
# Input: n = 4, k = 9
# Output: "2314"
# 
# 
#
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
 
        cand_ls = [i for i in range(1, n+1)]
        denominator = self.fac_helper(n-1)
        ret_ls = []
        k -= 1
        while True:
            if denominator == 0:
                idx = 0
            else:
                idx = k/denominator
            preceeding = cand_ls.pop(idx)
            ret_ls.append(preceeding)
            if not cand_ls:
                break
            k = k%denominator
            n -= 1
            denominator = self.fac_helper(n-1)

        return ''.join([str(x) for x in ret_ls])
            

    def fac_helper(self, n):

        if n == 1 or n == 0:
            return n
        else:
            return n*self.fac_helper(n-1)

