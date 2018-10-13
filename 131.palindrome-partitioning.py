#
# [131] Palindrome Partitioning
#
# https://leetcode.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (37.50%)
# Total Accepted:    135.5K
# Total Submissions: 360.7K
# Testcase Example:  '"aab"'
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome.
# 
# Return all possible palindrome partitioning of s.
# 
# Example:
# 
# 
# Input: "aab"
# Output:
# [
# ⁠ ["aa","b"],
# ⁠ ["a","a","b"]
# ]
# 
# 
#
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return [[]]

        res_ls = []
        for i in range(len(s)):
            if self.is_palindrome(s[:i+1]):
                for r in self.partition(s[i+1:]):
                  res_ls.append([s[:i+1]] + r)
        return res_ls

    def is_palindrome(self, s):
        return s == s[::-1]
