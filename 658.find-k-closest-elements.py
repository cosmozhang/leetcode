#
# [658] Find K Closest Elements
#
# https://leetcode.com/problems/find-k-closest-elements/description/
#
# algorithms
# Medium (35.67%)
# Total Accepted:    35K
# Total Submissions: 98.1K
# Testcase Example:  '[1,2,3,4,5]\n4\n3'
#
# 
# Given a sorted array, two integers k and x, find the k closest elements to x
# in the array.  The result should also be sorted in ascending order.
# If there is a tie,  the smaller elements are always preferred.
# 
# 
# Example 1:
# 
# Input: [1,2,3,4,5], k=4, x=3
# Output: [1,2,3,4]
# 
# 
# 
# 
# Example 2:
# 
# Input: [1,2,3,4,5], k=4, x=-1
# Output: [1,2,3,4]
# 
# 
# 
# Note:
# 
# The value k is positive and will always be smaller than the length of the
# sorted array.
# ⁠Length of the given array is positive and will not exceed 104
# ⁠Absolute value of elements in the array and x will not exceed 104
# 
# 
# 
# 
# 
# 
# UPDATE (2017/9/19):
# The arr parameter had been changed to an array of integers (instead of a list
# of integers). Please reload the code definition to get the latest changes.
# 
#
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        
        l = 0
        r = len(arr) - 1
        m = (l+r)/2
        while l<r:
            m = (l+r)/2
            if arr[m] > x:
                if m-1 > -1 and arr[m-1] <= x:
                    m -= 1
                    break
                else:
                    r = m-1
            elif arr[m] < x:
                if m+1 < len(arr) and arr[m+1] > x:
                    break
                elif m+1 < len(arr) and arr[m+1] == x:
                    m += 1
                    break
                else:
                    l = m+1
            else:
                break

        cnt = 1
        l = m
        r = m
        while cnt < k:
            if l == 0:
                r += 1
                cnt += 1
            elif r == len(arr) - 1:
                l -= 1
                cnt += 1
            else:
                if abs(arr[r+1]-x) < abs(arr[l-1]-x):
                    r += 1
                    cnt += 1
                    if cnt == k:
                        break
                else:
                    l -= 1
                    cnt += 1
                    if cnt == k:
                        break
                    
        return arr[l:r+1]
