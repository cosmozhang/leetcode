#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (38.89%)
# Total Accepted:    1.1M
# Total Submissions: 2.9M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
# 
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
# 
# Example:
# 
# 
# Given nums = [2, 7, 11, 15], target = 9,
# 
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
# 
# 
# 
# 
#
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        '''
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                s = nums[i] + nums[j]
                if s == target:
                    return [i, j]
        '''
        n2p = {}
        for idx, n in enumerate(nums):
            if n not in n2p:
                n2p[n] = [idx]
            else:
                n2p[n].append(idx)
                
        for k, poss in n2p.iteritems():
            s = target - k
            if s !=k:
                if s in n2p:
                    return [poss[0], n2p[s][0]]
            elif s == k:
                if len(poss) > 1:
                    return [poss[0], poss[1]]

        return []
