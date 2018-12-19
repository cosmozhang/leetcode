#
# [678] Valid Parenthesis String
#
# https://leetcode.com/problems/valid-parenthesis-string/description/
#
# algorithms
# Medium (30.70%)
# Total Accepted:    18.7K
# Total Submissions: 60.7K
# Testcase Example:  '"()"'
#
# 
# Given a string containing only three types of characters: '(', ')' and '*',
# write a function to check whether this string is valid. We define the
# validity of a string by these rules:
# 
# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left
# parenthesis '(' or an empty string.
# An empty string is also valid.
# 
# 
# 
# Example 1:
# 
# Input: "()"
# Output: True
# 
# 
# 
# Example 2:
# 
# Input: "(*)"
# Output: True
# 
# 
# 
# Example 3:
# 
# Input: "(*))"
# Output: True
# 
# 
# 
# Note:
# 
# The string size will be in the range [1, 100].
# 
# We need two stacks to record the idx, one for '(' n the other for '*'.
#
class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        '''
        if len(s) == 0:
            return True

        pstack = []
        sstack = []

        for idx, t in enumerate(s):
            if t == '(':
                pstack.append(idx)
            elif t == '*':
                sstack.append(idx)
            else:
                if len(pstack) == 0 and len(sstack) == 0:
                    return False
                elif len(pstack) == 0:
                    sstack.pop(-1)
                else:
                    pstack.pop(-1)

        while len(pstack) > 0:
            if len(sstack) == 0:
                return False
            elif sstack[-1] > pstack[-1]:
                sstack.pop(-1)
                pstack.pop(-1)
            else:
                return False
        return True
        '''

        if len(s) == 0:
            return True

        s_stack = []
        p_stack = []
        for idx, c in enumerate(s):
            if c == '(':
                p_stack.append(idx)
            elif c == '*':
                s_stack.append(idx)
            else:
                if len(p_stack) > 0:
                    p_stack.pop(-1)
                elif len(s_stack) > 0:
                    s_stack.pop(-1)
                else:
                    return False
        while len(p_stack) > 0:
            if len(s_stack) == 0:
                return False
            elif len(s_stack) > 0 and p_stack[-1] < s_stack[-1]:
                s_stack.pop(-1)
                p_stack.pop(-1)
            else:
                return False
        return True
        
