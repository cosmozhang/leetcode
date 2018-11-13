#
# [674] Longest Continuous Increasing Subsequence
#
# https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/
#
# algorithms
# Easy (43.09%)
# Total Accepted:    48.9K
# Total Submissions: 113.6K
# Testcase Example:  '[1,3,5,4,7]'
#
# 
# Given an unsorted array of integers, find the length of longest continuous
# increasing subsequence (subarray).
# 
# 
# Example 1:
# 
# Input: [1,3,5,4,7]
# Output: 3
# Explanation: The longest continuous increasing subsequence is [1,3,5], its
# length is 3. 
# Even though [1,3,5,7] is also an increasing subsequence, it's not a
# continuous one where 5 and 7 are separated by 4. 
# 
# 
# 
# Example 2:
# 
# Input: [2,2,2,2,2]
# Output: 1
# Explanation: The longest continuous increasing subsequence is [2], its length
# is 1. 
# 
# 
# 
# Note:
# Length of the array will not exceed 10,000.
# 
#
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return 0
        if len(nums) == 1:
            return 1
        
        dp = [1 for _ in range(len(nums))]

        for i, num in enumerate(nums):

            if i > 0:
                if nums[i] > nums[i-1]:
                    dp[i] = dp[i-1]+1

        return max(dp)
