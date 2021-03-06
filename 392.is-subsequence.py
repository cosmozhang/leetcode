#
# [392] Is Subsequence
#
# https://leetcode.com/problems/is-subsequence/description/
#
# algorithms
# Medium (45.45%)
# Total Accepted:    71.1K
# Total Submissions: 156.3K
# Testcase Example:  '"abc"\n"ahbgdc"'
#
# 
# Given a string s and a string t, check if s is subsequence of t.
# 
# 
# 
# You may assume that there is only lower case English letters in both s and t.
# t is potentially a very long (length ~= 500,000) string, and s is a short
# string (
# 
# 
# A subsequence of a string is a new string which is formed from the original
# string by deleting some (can be none) of the characters without disturbing
# the relative positions of the remaining characters. (ie, "ace" is a
# subsequence of "abcde" while "aec" is not).
# 
# 
# Example 1:
# s = "abc", t = "ahbgdc"
# 
# 
# Return true.
# 
# 
# Example 2:
# s = "axc", t = "ahbgdc"
# 
# 
# Return false.
# 
# 
# Follow up:
# If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you
# want to check one by one to see if T has its subsequence. In this scenario,
# how would you change your code?
# 
# Credits:Special thanks to @pbrother for adding this problem and creating all
# test cases.
#
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        
        if len(t) == 0:
            return False
        
        '''
        idx = 0
        for c in s:
            if idx > len(t) - 1:
                return False
            while t[idx] != c:
                idx += 1
                if idx > len(t)-1:
                    return False
            idx += 1

        return True
        '''

        # for follow up

        char2idx = {}

        for i, c in enumerate(t):
            if c not in char2idx:
                char2idx[c] = [i]
            else:
                char2idx[c] += [i]

        prev_pos = -1

        for c in s:
            if c not in char2idx:
                return False
            idx = self.bsearch(char2idx[c], prev_pos)
            if idx != -1:
                prev_pos = idx
            else:
                return False

        return True

    def bsearch(self, ls, prev):

        # find the 1st idx in ls that is larger than prev

        l = 0
        r = len(ls)-1

        while l < r:
            m = (l+r)/2
            if ls[m]<=prev:
                l = m + 1
            else:
                r = m
                
        if ls[l] <= prev:
            return -1
        else:
            return ls[l]

        
        
