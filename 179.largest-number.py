#
# [179] Largest Number
#
# https://leetcode.com/problems/largest-number/description/
#
# algorithms
# Medium (23.37%)
# Total Accepted:    100.9K
# Total Submissions: 420.4K
# Testcase Example:  '[10,2]'
#
# Given a list of non negative integers, arrange them such that they form the
# largest number.
# 
# Example 1:
# 
# 
# Input: [10,2]
# Output: "210"
# 
# Example 2:
# 
# 
# Input: [3,30,34,5,9]
# Output: "9534330"
# 
# 
# Note: The result may be very large, so you need to return a string instead of
# an integer.
# 
#
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        
        def mycmp(a, b):
            '''
            if a+b > b+a:
                return 1
            elif a+b < b+a:
                return -1
            else:
                return 0
            '''
            return 1 if a+b > b+a else -1

        str_nums = map(str, nums)
        s = ''
        for item in reversed(sorted(str_nums, cmp = mycmp)):
            s += item
        return str(int(''.join(s)))

