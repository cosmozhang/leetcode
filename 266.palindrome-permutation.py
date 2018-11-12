#
# [266] Palindrome Permutation
#
# https://leetcode.com/problems/palindrome-permutation/description/
#
# algorithms
# Easy (58.96%)
# Total Accepted:    55.7K
# Total Submissions: 94.5K
# Testcase Example:  '"code"'
#
# Given a string, determine if a permutation of the string could form a
# palindrome.
# 
# Example 1:
# 
# 
# Input: "code"
# Output: false
# 
# Example 2:
# 
# 
# Input: "aab"
# Output: true
# 
# Example 3:
# 
# 
# Input: "carerac"
# Output: true
# 
#
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        count_dic = {}

        for c in s:
            if c in count_dic:
                count_dic[c]+=1
            else:
                count_dic[c]=1

        odd_count = 0

        for k, v in count_dic.iteritems():
            if v % 2 != 0:
                odd_count +=1

        if odd_count >1:
            return False
        else:
            return True
