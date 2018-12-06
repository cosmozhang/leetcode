#
# [350] Intersection of Two Arrays II
#
# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
#
# algorithms
# Easy (45.45%)
# Total Accepted:    150.8K
# Total Submissions: 331.6K
# Testcase Example:  '[1,2,2,1]\n[2,2]'
#
# Given two arrays, write a function to compute their intersection.
# 
# Example 1:
# 
# 
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# 
# 
# 
# Example 2:
# 
# 
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# 
# 
# Note:
# 
# 
# Each element in the result should appear as many times as it shows in both
# arrays.
# The result can be in any order.
# 
# 
# Follow up:
# 
# 
# What if the given array is already sorted? How would you optimize your
# algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is
# better?
# What if elements of nums2 are stored on disk, and the memory is limited such
# that you cannot load all elements into the memory at once?
# 
# 
#
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # two pointer
        '''
        nums1.sort()
        nums2.sort()

        u = 0
        v = 0

        res_ls = []
        while u < len(nums1) and v < len(nums2):
            if nums1[u] < nums2[v]:
                u+=1
            elif nums1[u] > nums2[v]:
                v +=1
            else:
                res_ls.append(nums1[u])
                u+=1
                v+=1
        return res_ls
        '''
        # hashmap
        '''
        count_map = {}

        if len(nums1) < len(nums2):
            to_map = nums1
            nums = nums2
        else:
            to_map = nums1
            nums = nums2

        for n in to_map:
            if n in count_map:
                count_map[n] += 1
            else:
                count_map[n] = 1

        ret_ls = []
        
        for t in nums:
            if t in count_map and count_map[t] > 0:
                ret_ls.append(t)
                count_map[t] -= 1

        return ret_ls
        '''
        # binary search
        nums1.sort()
        nums2.sort()

        
        
        l = 0
        r = len(nums2) - 1
        ret_ls = []
        for n in nums1:
            if l >= len(nums2):
                break
            idx = self.bi_search(n, nums2, l, r)
            if idx < len(nums2) and nums2[idx] == n:
                ret_ls.append(n)
                l = idx + 1

        return ret_ls

    def bi_search(self, tgt, nums, l, r):

        while l < r:

            m = (l+r) >> 1
            if nums[m] < tgt:
                l += 1
            elif nums[m] >= tgt:
                r = m

        return l
