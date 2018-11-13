#
# [246] Strobogrammatic Number
#
# https://leetcode.com/problems/strobogrammatic-number/description/
#
# algorithms
# Easy (41.04%)
# Total Accepted:    43.7K
# Total Submissions: 106.4K
# Testcase Example:  '"69"'
#
# A strobogrammatic number is a number that looks the same when rotated 180
# degrees (looked at upside down).
# 
# Write a function to determine if a number is strobogrammatic. The number is
# represented as a string.
# 
# Example 1:
# 
# 
# Input:  "69"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input:  "88"
# Output: true
# 
# Example 3:
# 
# 
# Input:  "962"
# Output: false
# 
#
class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """

        if len(num) == 0:
            return True

        if len(num) == 1:
            if num not in ['8', '0', '1']:
                return False
        
        for c in num:
            if c not in ['6', '9', '0', '8', '1']:
                return False

        l = len(num)/2
        tmp = list(num[:l])
        for i, c in enumerate(tmp):
            if c == '6':
                tmp[i] = '9'
            elif c == '9':
                tmp[i] = '6'

        newnum = ''.join(tmp) + num[l:]
        return newnum == newnum[::-1]
