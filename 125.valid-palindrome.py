#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (28.71%)
# Total Accepted:    274.8K
# Total Submissions: 955.7K
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# Given a string, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.
# 
# Note: For the purpose of this problem, we define empty string as valid
# palindrome.
# 
# Example 1:
# 
# 
# Input: "A man, a plan, a canal: Panama"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: "race a car"
# Output: false
# 
# 
#
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        valid_range = range(ord('a'), ord('a')+26) + range(ord('0'), ord('0')+10)
        s = filter(lambda x: x in map(chr, valid_range), list(s))
        
        return s == s[::-1]
