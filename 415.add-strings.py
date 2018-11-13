#
# [415] Add Strings
#
# https://leetcode.com/problems/add-strings/description/
#
# algorithms
# Easy (42.28%)
# Total Accepted:    74.1K
# Total Submissions: 175.1K
# Testcase Example:  '"0"\n"0"'
#
# Given two non-negative integers num1 and num2 represented as string, return
# the sum of num1 and num2.
# 
# Note:
# 
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to
# integer directly.
# 
# 
#
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
                
        num1_rstr = num1[::-1]
        num2_rstr = num2[::-1]
        t = 0
        l1, l2 = len(num1_rstr), len(num2_rstr)

        res_ls = []
        i = 0
        while i < max(l1, l2) or t > 0 :
            if i < l1:
                n1 = int(num1_rstr[i])
            else:
                n1 = 0
            if i < l2:
                n2 = int(num2_rstr[i])
            else:
                n2 = 0
            i += 1
            s = n1 + n2 + t
            if s >=10:
                t = 1
                res_ls += [s-10]
            else:
                t = 0
                res_ls += [s]
        return ''.join([str(v) for v in res_ls[::-1]])
