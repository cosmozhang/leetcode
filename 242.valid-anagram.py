#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# algorithms
# Easy (49.36%)
# Total Accepted:    262.9K
# Total Submissions: 532.2K
# Testcase Example:  '"anagram"\n"nagaram"'
#
# Given two strings s and t , write a function to determine if t is an anagram
# of s.
# 
# Example 1:
# 
# 
# Input: s = "anagram", t = "nagaram"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "rat", t = "car"
# Output: false
# 
# 
# Note:
# You may assume the string contains only lowercase alphabets.
# 
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your
# solution to such case?
# 
#
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        return sorted(list(s)) == sorted(list(t))
