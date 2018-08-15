# coding: --utf8--
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (21.93%)
# Total Accepted:    361.5K
# Total Submissions: 1.6M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an array nums of n integers, are there elements a, b, c in nums such
# that a + b + c = 0? Find all unique triplets in the array which gives the sum
# of zero.
#
# Note:
#
# The solution set must not contain duplicate triplets.
#
# Example:
#
#
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
#
#
#
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res_ls =[]
        m_rem = None
        if len(nums) < 3:
            return []
        else:
            sorted_ls = sorted(nums)
            for s_idx in range(len(nums)-2):
                if s_idx - 1 >= 0 and sorted_ls[s_idx] == sorted_ls[s_idx-1]:
                    continue
                m_idx = s_idx + 1
                e_idx = len(sorted_ls) - 1
                while m_idx < e_idx:
                    if sorted_ls[s_idx] + sorted_ls[e_idx] + sorted_ls[m_idx] == 0:
                        res_ls.append([sorted_ls[s_idx], sorted_ls[m_idx], sorted_ls[e_idx]])
                        while m_idx < e_idx and sorted_ls[m_idx] == sorted_ls[m_idx+1]:
                            m_idx += 1
                        while e_idx > m_idx and sorted_ls[e_idx] == sorted_ls[e_idx-1]:
                            e_idx -= 1
                        m_idx += 1
                        e_idx -= 1
                    elif sorted_ls[s_idx] + sorted_ls[e_idx] + sorted_ls[m_idx] > 0:
                        e_idx -= 1
                    elif sorted_ls[s_idx] + sorted_ls[e_idx] + sorted_ls[m_idx] < 0:
                        m_idx += 1
            return res_ls
