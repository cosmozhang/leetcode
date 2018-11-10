#
# [344] Reverse String
#
# https://leetcode.com/problems/reverse-string/description/
#
# algorithms
# Easy (61.76%)
# Total Accepted:    318.3K
# Total Submissions: 515.4K
# Testcase Example:  '"hello"'
#
# Write a function that takes a string as input and returns the string
# reversed.
# 
# Example 1:
# 
# 
# 
# Input: "hello"
# Output: "olleh"
# 
# 
# 
# Example 2:
# 
# 
# Input: "A man, a plan, a canal: Panama"
# Output: "amanaP :lanac a ,nalp a ,nam A"
# 
# 
# 
# 
#
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        return s[::-1]
