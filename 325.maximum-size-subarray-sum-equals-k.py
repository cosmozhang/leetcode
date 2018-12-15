#
# [325] Maximum Size Subarray Sum Equals k
#
# https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/description/
#
# algorithms
# Medium (43.81%)
# Total Accepted:    65.6K
# Total Submissions: 149.7K
# Testcase Example:  '[1,-1,5,-2,3]\n3'
#
# Given an array nums and a target value k, find the maximum length of a
# subarray that sums to k. If there isn't one, return 0 instead.
# 
# Note:
# The sum of the entire nums array is guaranteed to fit within the 32-bit
# signed integer range.
# 
# Example 1:
# 
# 
# Input: nums = [1, -1, 5, -2, 3], k = 3
# Output: 4 
# Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
# 
# 
# Example 2:
# 
# 
# Input: nums = [-2, -1, 2, 1], k = 1
# Output: 2 
# Explanation: The subarray [-1, 2] sums to 1 and is the longest.
# 
# Follow Up:
# Can you do it in O(n) time?
# 
#
class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        '''
        ret = 0
        s = 0
        idx_dic = {0:-1}

        for idx, v in enumerate(nums):
            s += v
            if s not in idx_dic:
                idx_dic[s] = idx

            if s - k in idx_dic:
                ret = max(ret, idx-idx_dic[s-k])
        return ret
        '''

        s = 0
        max_l = 0
        idx_dic = {0:-1}

        for idx, num in enumerate(nums):
            s += num
            t = s - k
            if t in idx_dic:
                max_l = max(max_l, idx - idx_dic[t])
            if s not in idx_dic:
                idx_dic[s] = idx

        return max_l
            
        
