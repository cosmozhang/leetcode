#
# [150] Evaluate Reverse Polish Notation
#
# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
#
# algorithms
# Medium (29.98%)
# Total Accepted:    132.7K
# Total Submissions: 442.5K
# Testcase Example:  '["2","1","+","3","*"]'
#
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# 
# Valid operators are +, -, *, /. Each operand may be an integer or another
# expression.
# 
# Note:
# 
# 
# Division between two integers should truncate toward zero.
# The given RPN expression is always valid. That means the expression would
# always evaluate to a result and there won't be any divide by zero
# operation.
# 
# 
# Example 1:
# 
# 
# Input: ["2", "1", "+", "3", "*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# 
# 
# Example 2:
# 
# 
# Input: ["4", "13", "5", "/", "+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# 
# 
# Example 3:
# 
# 
# Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# Output: 22
# Explanation: 
# ⁠ ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
# 
# 
#
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if len(tokens) == 1:
            return int(tokens[0])
        
        def operfunc(a, b, o):
            if o == '+':
                return a + b
            elif o == '*':
                return a * b
            elif o == '/':
                if (a < 0 and b >0):
                    return -(abs(a)/b)
                elif (a >0 and b <0):
                    return -(a/abs(b))
                else:
                    return a / b
            elif o == '-':
                return a - b

        s = []
        oper_set = ('-', '*', '/', '+')
        for i, t in enumerate(tokens):
            if t in oper_set:
                b = s.pop(-1)
                a = s.pop(-1)
                v = operfunc(a, b, t)
                s.append(v)
            else:
                s.append(int(t))

        return s[0]
                
                
