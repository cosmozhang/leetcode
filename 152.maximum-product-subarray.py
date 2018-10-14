#
# [152] Maximum Product Subarray
#
# https://leetcode.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (27.61%)
# Total Accepted:    165.1K
# Total Submissions: 598K
# Testcase Example:  '[2,3,-2,4]'
#
# Given an integer array nums, find the contiguous subarray within an array
# (containing at least one number) which has the largest product.
# 
# Example 1:
# 
# 
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# 
# 
# Example 2:
# 
# 
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
# 
#
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        if len(nums)==1:
            return nums[0]
        
        res_ls = [[None for i in range(2)] for j in range(len(nums))]

        res_ls[0][0], res_ls[0][1] = nums[0], nums[0]

        max_v = nums[0]
        for i in range(1, len(nums)):
            max_c = max(res_ls[i-1][0] * nums[i], res_ls[i-1][1] * nums[i], nums[i])
            min_c = min(res_ls[i-1][0] * nums[i], res_ls[i-1][1] * nums[i], nums[i])
            res_ls[i][0] = max_c
            res_ls[i][1] = min_c
            if max_c > max_v:
                max_v = max_c
        return max_v
            
