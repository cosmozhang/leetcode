#
# [560] Subarray Sum Equals K
#
# https://leetcode.com/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (40.54%)
# Total Accepted:    61.6K
# Total Submissions: 151.8K
# Testcase Example:  '[1,1,1]\n2'
#
# Given an array of integers and an integer k, you need to find the total
# number of continuous subarrays whose sum equals to k.
# 
# Example 1:
# 
# Input:nums = [1,1,1], k = 2
# Output: 2
# 
# 
# 
# Note:
# 
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the
# integer k is [-1e7, 1e7].
# 
# 
# 
#
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        '''
        s = 0
        sum_idx_dic = {0:1}
        cnt = 0
        for idx, num in enumerate(nums):
            s += num
            t = s - k
            if t in sum_idx_dic:
                cnt += sum_idx_dic[t]
            
            if s not in sum_idx_dic:
                sum_idx_dic[s] = 1
            else:
                sum_idx_dic[s] += 1

        return cnt
        '''

        
        
        s = 0
        cnt = 0
        sum2times = {0:1}

        for num in nums:
            s += num
            if s-k in sum2times:
                cnt += sum2times[s-k]

            if s in sum2times:
                sum2times[s] += 1
            else:
                sum2times[s] = 1

        return cnt
