#
# [227] Basic Calculator II
#
# https://leetcode.com/problems/basic-calculator-ii/description/
#
# algorithms
# Medium (31.72%)
# Total Accepted:    86K
# Total Submissions: 271.2K
# Testcase Example:  '"3+2*2"'
#
# Implement a basic calculator to evaluate a simple expression string.
# 
# The expression string contains only non-negative integers, +, -, *, /
# operators and empty spaces  . The integer division should truncate toward
# zero.
# 
# Example 1:
# 
# 
# Input: "3+2*2"
# Output: 7
# 
# 
# Example 2:
# 
# 
# Input: " 3/2 "
# Output: 1
# 
# Example 3:
# 
# 
# Input: " 3+5 / 2 "
# Output: 5
# 
# 
# Note:
# 
# 
# You may assume that the given expression is always valid.
# Do not use the eval built-in library function.
# 
#
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        oper = ['+', '-', '*', '/']

        s = list(s.replace(' ', ''))
        stack = []
        prev = None

        a = 0
        for idx, n in enumerate(s):
            
            if n not in oper:
                a = a*10+int(n)

            if idx == len(s)-1 or n in oper:
                if prev == '+' or prev == None:
                    stack.append(a)
                elif prev == '-':
                    stack.append(-a)

                elif prev == '*':
                    b = stack.pop(-1)
                    stack.append(a * b)

                elif prev == '/':
                    b = stack.pop(-1)
                    if b/a>=0:
                        u = b/a
                    else:
                        u = int(1.0*b/a)
                    stack.append(u)
                    
                prev = n
                a = 0

        return sum(stack)
                
