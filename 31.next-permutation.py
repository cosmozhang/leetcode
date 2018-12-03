#coding: --utf8--
# [31] Next Permutation
#
# https://leetcode.com/problems/next-permutation/description/
#
# algorithms
# Medium (29.18%)
# Total Accepted:    168.5K
# Total Submissions: 577.2K
# Testcase Example:  '[1,2,3]'
#
# Implement next permutation, which rearranges numbers into the
# lexicographically next greater permutation of numbers.
#
# If such arrangement is not possible, it must rearrange it as the lowest
# possible order (ie, sorted in ascending order).
#
# The replacement must be in-place and use only constant extra memory.
#
# Here are some examples. Inputs are in the left-hand column and its
# corresponding outputs are in the right-hand column.
#
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
#
#
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        '''
        if len(nums) == 1:
            nums = nums
        idx = len(nums) - 1
        prev = nums[idx]
        while idx > 0:
            if nums[idx-1] < prev:
                break
            idx -= 1
            prev = nums[idx]
        if idx == 0:
            nums[:] = nums[::-1]
        else:
            toswap_idx = idx - 1
            if nums[-1] > nums[toswap_idx]:
                tobeswap_idx = len(nums) - 1
            else:
                for j in range(idx, len(nums)):
                    if nums[j] <= nums[toswap_idx]:
                        tobeswap_idx = j-1 # the 1st num > nums[toswap_idx]
                        break
            nums[toswap_idx], nums[tobeswap_idx] = nums[tobeswap_idx], nums[toswap_idx]
            nums[idx:] = nums[idx:][::-1]
        '''

        
        to_right_idx = -1
        for i in range(len(nums) - 1, -1, -1):
            if i-1 > -1 and nums[i-1] < nums[i]:
                to_right_idx = i-1
                break

        if to_right_idx == -1:
            nums[:] = nums[::-1]
        else:
            r = nums[to_right_idx]
            for j in range(len(nums) - 1, to_right_idx, -1):
                if nums[j] > r:
                    to_left_idx = j
                    break
            nums[to_left_idx], nums[to_right_idx] = nums[to_right_idx], nums[to_left_idx]
            nums[to_right_idx+1:] = nums[to_right_idx+1:][::-1]
