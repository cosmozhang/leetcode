#
# [496] Next Greater Element I
#
# https://leetcode.com/problems/next-greater-element-i/description/
#
# algorithms
# Easy (57.41%)
# Total Accepted:    73.6K
# Total Submissions: 128.2K
# Testcase Example:  '[4,1,2]\n[1,3,4,2]'
#
# 
# You are given two arrays (without duplicates) nums1 and nums2 where nums1’s
# elements are subset of nums2. Find all the next greater numbers for nums1's
# elements in the corresponding places of nums2. 
# 
# 
# 
# The Next Greater Number of a number x in nums1 is the first greater number to
# its right in nums2. If it does not exist, output -1 for this number.
# 
# 
# Example 1:
# 
# Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
# Output: [-1,3,-1]
# Explanation:
# ⁠   For number 4 in the first array, you cannot find the next greater number
# for it in the second array, so output -1.
# ⁠   For number 1 in the first array, the next greater number for it in the
# second array is 3.
# ⁠   For number 2 in the first array, there is no next greater number for it
# in the second array, so output -1.
# 
# 
# 
# Example 2:
# 
# Input: nums1 = [2,4], nums2 = [1,2,3,4].
# Output: [3,-1]
# Explanation:
# ⁠   For number 2 in the first array, the next greater number for it in the
# second array is 3.
# ⁠   For number 4 in the first array, there is no next greater number for it
# in the second array, so output -1.
# 
# 
# 
# 
# Note:
# 
# All elements in nums1 and nums2 are unique.
# The length of both nums1 and nums2 would not exceed 1000.
# 
# 
#
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(findNums) == 0 or len(nums) == 0:
            return []
        
        next_g_dic = {}
        for n in nums:
            next_g_dic[n] = -1

        s = [nums[0]]
        for n in nums[1:]:
            while s and n>s[-1]:
                next_g_dic[s[-1]] = n
                s.pop(-1)
            s.append(n)
        
        
        return [next_g_dic[j] for j in findNums]
                