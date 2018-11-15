#
# [260] Single Number III
#
# https://leetcode.com/problems/single-number-iii/description/
#
# algorithms
# Medium (55.06%)
# Total Accepted:    94K
# Total Submissions: 170.7K
# Testcase Example:  '[1,2,1,3,2,5]'
#
# Given an array of numbers nums, in which exactly two elements appear only
# once and all the other elements appear exactly twice. Find the two elements
# that appear only once.
# 
# Example:
# 
# 
# Input:  [1,2,1,3,2,5]
# Output: [3,5]
# 
# Note:
# 
# 
# The order of the result is not important. So in the above example, [5, 3] is
# also correct.
# Your algorithm should run in linear runtime complexity. Could you implement
# it using only constant space complexity?
# 
#
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        axorb = 0
        num1, num2 = 0, 0
        for num in nums:
            axorb ^= num

        mask = 1
        while mask & axorb == 0:
            mask = mask << 1

        for num in nums:
            if num & mask:
                num1 ^= num
            else:
                print num&mask
                num2 ^= num

        return [num1, num2]
