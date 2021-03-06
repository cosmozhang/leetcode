# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (34.70%)
# Total Accepted:    418.5K
# Total Submissions: 1.2M
# Testcase Example:  '"()"'
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
# 
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# 
# 
# Note that an empty string is also considered valid.
# 
# Example 1:
# 
# 
# Input: "()"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: "()[]{}"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: "(]"
# Output: false
# 
# 
# Example 4:
# 
# 
# Input: "([)]"
# Output: false
# 
# 
# Example 5:
# 
# 
# Input: "{[]}"
# Output: true
# 
# 
#
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        '''
        if not s:
            return True
        pair_dic = {')':'(', ']':'[', '}':'{'}
        
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if not stack:
                    return False
                else:
                    p = stack.pop(-1)
                    if p != pair_dic[c]:
                        return False
                    
        if stack:
            return False
        else:
            return True
        '''

        p2dic = {')':'(', ']':'[', '}': '{'}

        if len(s) == 0:
            return True

        s_ls = list(s)
        stack = []
        while len(s_ls)>0:
            p = s_ls.pop(0)
            if len(stack) > 0:
                if p in p2dic and p2dic[p] == stack[-1]:
                    stack.pop(-1)
                else:
                    stack.append(p)
            else:
                stack.append(p)
        if len(stack) == 0 and len(s_ls) == 0:
            return True
        else:
            return False

        
