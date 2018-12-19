#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary/description/
#
# algorithms
# Easy (35.98%)
# Total Accepted:    239.1K
# Total Submissions: 663.4K
# Testcase Example:  '"11"\n"1"'
#
# Given two binary strings, return their sum (also a binary string).
#
# The input strings are both non-empty and contains only characters 1 or 0.
#
# Example 1:
#
#
# Input: a = "11", b = "1"
# Output: "100"
#
# Example 2:
#
#
# Input: a = "1010", b = "1011"
# Output: "10101"
#
#
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        '''
        a = map(int, list(a))
        b = map(int, list(b))

        c = []

        la, lb = len(a), len(b)

        i = 0
        cache = 0
        while True:
            if i < la and i < lb:
                a1, b1 = a.pop(-1), b.pop(-1)
                s = a1+b1+cache
                if s > 1:
                    c.append(s-2)
                    cache = 1
                else:
                    c.append(s)
                    cache = 0
            elif la <= i and i < lb:
                b1 = b.pop(-1)
                s = b1 + cache
                if s == 2:
                    c.append(0)
                    cache = 1
                else:
                    c.append(s)
                    cache = 0
            elif lb <= i and i < la:
                a1 = a.pop(-1)
                s = a1 + cache
                if s == 2:
                    c.append(0)
                    cache = 1
                else:
                    c.append(s)
                    cache = 0
            else:
                break
            i += 1
        if cache == 1:
            c.append(1)

        return ''.join(map(str, c[::-1]))

        '''
        a_rls = [int(c) for c in a][::-1]
        b_rls = [int(c) for c in b][::-1]

        c_rls = []
        carry = 0

        while len(a_rls) > 0 or len(b_rls) > 0:

            a_num = 0
            if len(a_rls) > 0:
                a_num = a_rls.pop(0)

            b_num = 0
            if len(b_rls) > 0:
                b_num = b_rls.pop(0)

            s = a_num + b_num + carry

            if s<2:
                carry = 0
                c_rls.append(s)
            else:
                carry = 1
                c_rls.append(s-2)

        if carry == 1:
            c_rls.append(1)

        return ''.join(map(str, c_rls[::-1]))



