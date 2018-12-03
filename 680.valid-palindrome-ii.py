#
# [680] Valid Palindrome II
#
# https://leetcode.com/problems/valid-palindrome-ii/description/
#
# algorithms
# Easy (32.92%)
# Total Accepted:    50.6K
# Total Submissions: 153.7K
# Testcase Example:  '"aba"'
#
# 
# Given a non-empty string s, you may delete at most one character.  Judge
# whether you can make it a palindrome.
# 
# 
# Example 1:
# 
# Input: "aba"
# Output: True
# 
# 
# 
# Example 2:
# 
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
# 
# 
# 
# Note:
# 
# The string will only contain lowercase characters a-z.
# The maximum length of the string is 50000.
# 
# 
#
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        '''
        if len(s) == 0:
            return True
        
        l = 0
        r = len(s)-1

        while l < r:
            if s[l] != s[r]:
                no_l_s = s[:l]+s[l+1:]
                no_r_s = s[:r]+s[r+1:]
                if no_l_s == no_l_s[::-1] or no_r_s == no_r_s[::-1]:
                    return True
                else:
                    return False
            l+=1
            r-=1

        return True
        '''

        l = 0
        r = len(s) -1
        while l < r:

            if s[l] ==s[r]:
                l += 1
                r -= 1
            else:
                if self.helper(l+1, r, s) or self.helper(l, r-1, s):
                    return True
                else:
                    return False

        return True
    
    def helper(self, l, r, s):

        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True
        
