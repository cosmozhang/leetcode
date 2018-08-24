#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (49.53%)
# Total Accepted:    235.5K
# Total Submissions: 474.3K
# Testcase Example:  '3'
#
# 
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
# 
# 
# 
# For example, given n = 3, a solution set is:
# 
# 
# [
# ⁠ "((()))",
# ⁠ "(()())",
# ⁠ "(())()",
# ⁠ "()(())",
# ⁠ "()()()"
# ]
# 
#


# use dynamic programming
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp_tb = [[] for i in range(n+1)]

        dp_tb[0] = ['']
        for i in range(1, n+1):
            for j in range(i):
                dp_tb[i].extend(['(' + x + ')' + y for x in dp_tb[j] for y in dp_tb[i-j-1]])
        return dp_tb[n]
