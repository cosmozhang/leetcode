#
# [43] Multiply Strings
#
# https://leetcode.com/problems/multiply-strings/description/
#
# algorithms
# Medium (28.44%)
# Total Accepted:    153K
# Total Submissions: 535.8K
# Testcase Example:  '"2"\n"3"'
#
# Given two non-negative integers num1 and num2 represented as strings, return
# the product of num1 and num2, also represented as a string.
# 
# Example 1:
# 
# 
# Input: num1 = "2", num2 = "3"
# Output: "6"
# 
# Example 2:
# 
# 
# Input: num1 = "123", num2 = "456"
# Output: "56088"
# 
# 
# Note:
# 
# 
# The length of both num1 and num2 is < 110.
# Both num1 and num2 contain only digits 0-9.
# Both num1 and num2 do not contain any leading zero, except the number 0
# itself.
# You must not use any built-in BigInteger library or convert the inputs to
# integer directly.
# 
# 
#
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        '''
        rev_nums2 = num2[::-1]
        rev_nums1 = num1[::-1]
        s = 0
        for i in range(len(rev_nums2)):
            temp = 0
            for j in range(len(rev_nums1)):
                temp += int(rev_nums2[i]) * int(rev_nums1[j]) * (10**j)
            s += temp * (10**i)
        return str(s)
        '''


        r_num1 = [int(n) for n in num1][::-1]
        r_num2 = [int(n) for n in num2][::-1]

        p = 0
        for i in range(len(r_num1)):
            tmp = 0
            for j in range(len(r_num2)):
                tmp += r_num1[i] * r_num2[j] * 10**j
            p += tmp * 10**i

        return str(p)
            
        
