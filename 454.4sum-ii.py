#
# [454] 4Sum II
#
# https://leetcode.com/problems/4sum-ii/description/
#
# algorithms
# Medium (48.77%)
# Total Accepted:    48.8K
# Total Submissions: 100K
# Testcase Example:  '[1,2]\n[-2,-1]\n[-1,2]\n[0,2]'
#
# Given four lists A, B, C, D of integer values, compute how many tuples (i, j,
# k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
# 
# To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤
# N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is
# guaranteed to be at most 231 - 1.
# 
# Example:
# 
# Input:
# A = [ 1, 2]
# B = [-2,-1]
# C = [-1, 2]
# D = [ 0, 2]
# 
# Output:
# 2
# 
# Explanation:
# The two tuples are:
# 1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
# 
# 
#
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        ab_sum = {}
        for i in range(len(A)):
            for j in range(len(B)):
                s = A[i] + B[j]
                if s not in ab_sum:
                    ab_sum[s] = 1
                else:
                    ab_sum[s] += 1

        cd_sum = {}
        for k in range(len(C)):
            for l in range(len(D)):
                s = C[k] + D[l]
                if s not in cd_sum:
                    cd_sum[s] = 1
                else:
                    cd_sum[s] += 1
        cnt = 0
        for k, v in ab_sum.iteritems():
            if -k in cd_sum:
                cnt += v * cd_sum[-k]
        return cnt
             
