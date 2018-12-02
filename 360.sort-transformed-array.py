#
# [360] Sort Transformed Array
#
# https://leetcode.com/problems/sort-transformed-array/description/
#
# algorithms
# Medium (45.90%)
# Total Accepted:    23.2K
# Total Submissions: 50.4K
# Testcase Example:  '[-4,-2,2,4]\n1\n3\n5'
#
# Given a sorted array of integers nums and integer values a, b and c. Apply a
# quadratic function of the form f(x) = ax2 + bx + c to each element x in the
# array.
# 
# The returned array must be in sorted order.
# 
# Expected time complexity: O(n)
# 
# 
# Example 1:
# 
# 
# Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
# Output: [3,9,15,33]
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
# Output: [-23,-5,1,7]
# 
# 
# 
#
class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []

        ret_ls = []

        l = 0
        r = len(nums)-1
        
        if a < 0 or (a==0 and b >=0):

            while l <= r:
                ql = self.qfunc(nums[l], a, b, c)
                qr = self.qfunc(nums[r], a, b, c)
                if ql < qr:
                    ret_ls.append(ql)
                    l += 1
                else:
                    ret_ls.append(qr)
                    r -= 1
            
            return ret_ls
        
        elif a > 0 or (a==0 and b < 0):

            while l <= r:
                ql = self.qfunc(nums[l], a, b, c)
                qr = self.qfunc(nums[r], a, b, c)
                if ql > qr:
                    ret_ls.append(ql)
                    l += 1
                else:
                    ret_ls.append(qr)
                    r -= 1
            return ret_ls[::-1]
        

    def qfunc(self, x, a, b, c):

        return a*x**2 + b*x + c
