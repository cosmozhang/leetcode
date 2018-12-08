# -*- coding: utf-8 -*-
# [88] Merge Sorted Array
#
# https://leetcode.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (33.48%)
# Total Accepted:    282.7K
# Total Submissions: 843.8K
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as
# one sorted array.
#
# Note:
#
#
# The number of elements initialized in nums1 and nums2 are m and n
# respectively.
# You may assume that nums1 has enough space (size that is greater or equal to
# m + n) to hold additional elements from nums2.
#
#
# Example:
#
#
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# Output: [1,2,2,3,5,6]
#
# Start from the last empty position of the 1st array
#
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        '''
        idx = m + n -1
        l = m-1
        r = n-1
        while l >=0 and r >=0:
            if nums1[l] > nums2[r]:
                nums1[idx] = nums1[l]
                l -= 1
            else:
                nums1[idx] = nums2[r]
                r -= 1
            idx -= 1
        if l < 0:
            nums1[:idx+1] = nums2[:r+1]

        '''

        idx = m+n-1

        l = m - 1
        r = n - 1

        while l > -1 and r > -1:
            if nums1[l] > nums2[r]:
                nums1[idx] = nums1[l]
                idx -= 1
                l -= 1
            else:
                nums1[idx] = nums2[r]
                idx -= 1
                r -= 1
        if l < 0:
            nums1[:idx+1] = nums2[:r+1]
