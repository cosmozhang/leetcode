#
# [647] Palindromic Substrings
#
# https://leetcode.com/problems/palindromic-substrings/description/
#
# algorithms
# Medium (54.51%)
# Total Accepted:    65.2K
# Total Submissions: 119.5K
# Testcase Example:  '"abc"'
#
# 
# Given a string, your task is to count how many palindromic substrings in this
# string.
# 
# 
# 
# The substrings with different start indexes or end indexes are counted as
# different substrings even they consist of same characters. 
# 
# 
# Example 1:
# 
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# 
# 
# 
# Example 2:
# 
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
# 
# 
# 
# Note:
# 
# The input string length won't exceed 1000.
# 
# 
#
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        
        s_l = len(s)
        return sum([self.count_odd(s, i) for i in range(s_l)]) + sum([self.count_even(s, i) for i in range(1, s_l)])

    def count_odd(self, s, i):
        c = 1
        l = i-1
        r = i+1

        s_l = len(s)
        while l>=0 and r <= s_l-1:
            if s[l] == s[r]:
                c +=1
            else:
                break
            l -= 1
            r += 1
        return c

    def count_even(self, s, i):
        c = 0
        l = i-1
        r = i
        
        s_l = len(s)
        while l>=0 and r <= s_l-1:
            if s[l] == s[r]:
                c+=1
            else:
                break
            l -= 1
            r += 1
        return c
