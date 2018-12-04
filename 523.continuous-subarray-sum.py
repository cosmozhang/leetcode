#
# [523] Continuous Subarray Sum
#
# https://leetcode.com/problems/continuous-subarray-sum/description/
#
# algorithms
# Medium (23.81%)
# Total Accepted:    51.1K
# Total Submissions: 214.7K
# Testcase Example:  '[23,2,4,6,7]\n6'
#
# 
# Given a list of non-negative numbers and a target integer k, write a function
# to check if the array has a continuous subarray of size at least 2 that sums
# up to the multiple of k, that is, sums up to n*k where n is also an
# integer.
# 
# 
# 
# Example 1:
# 
# Input: [23, 2, 4, 6, 7],  k=6
# Output: True
# Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to
# 6.
# 
# 
# 
# 
# Example 2:
# 
# Input: [23, 2, 6, 4, 7],  k=6
# Output: True
# Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and
# sums up to 42.
# 
# 
# 
# Note:
# 
# The length of the array won't exceed 10,000.
# You may assume the sum of all the numbers is in the range of a signed 32-bit
# integer.
# 
# use mod
#
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        s = 0

        mod2idx = {0:-1}

        for idx, num in enumerate(nums):
            
            s += num
            if k == 0:
                if s in mod2idx and mod2idx[s] < idx -1:
                    return True
                if s not in mod2idx:
                    mod2idx[s] = idx
            else:
                t = s%k
                if t in mod2idx and mod2idx[t] < idx -1:
                    return True
                if t not in mod2idx:
                    mod2idx[t] = idx

        return False
