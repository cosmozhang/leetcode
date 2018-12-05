#
# [215] Kth Largest Element in an Array
#
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (43.19%)
# Total Accepted:    269.1K
# Total Submissions: 619.8K
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# Find the kth largest element in an unsorted array. Note that it is the kth
# largest element in the sorted order, not the kth distinct element.
# 
# Example 1:
# 
# 
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# 
# 
# Example 2:
# 
# 
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ array's length.
# 
#
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        '''
        sorted_nums = sorted(nums, reverse=True)
        
        return sorted_nums[k-1]
        '''
        p = nums[0]
        tmp = nums[1:]
        l, r = [], []
        while True:
            for n in tmp:
                if n<= p:
                    l.append(n)
                else:
                    r.append(n)
            if len(r) == k-1:
                break
            elif len(r) >k-1:
                p = r[0]
                tmp = r[1:]
            else:
                k = k - 1- len(r)
                p = l[0]
                tmp = l[1:]
            l, r = [], []

        return p
        
