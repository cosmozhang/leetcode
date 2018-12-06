#
# [349] Intersection of Two Arrays
#
# https://leetcode.com/problems/intersection-of-two-arrays/description/
#
# algorithms
# Easy (50.74%)
# Total Accepted:    170.6K
# Total Submissions: 336.2K
# Testcase Example:  '[1,2,2,1]\n[2,2]'
#
# Given two arrays, write a function to compute their intersection.
#
# Example 1:
#
#
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
#
#
#
# Example 2:
#
#
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
#
#
# Note:
#
#
# Each element in the result must be unique.
# The result can be in any order.
#
#
#
#
#
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        '''
        return list(set(nums1) & set(nums2))
        '''

        s_nums1 = sorted(nums1)

        res_set = set()

        for n in nums2:
            l, r = 0, len(nums1) - 1
            while l <= r:
                m = (l+r) >> 1
                if s_nums1[m] == n:
                    res_set.add(n)
                    break
                elif s_nums1[m] < n:
                    l = m+1
                else:
                    r = m-1

        return list(res_set)
