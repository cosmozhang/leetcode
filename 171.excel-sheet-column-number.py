#
# [171] Excel Sheet Column Number
#
# https://leetcode.com/problems/excel-sheet-column-number/description/
#
# algorithms
# Easy (49.87%)
# Total Accepted:    190.4K
# Total Submissions: 381.5K
# Testcase Example:  '"A"'
#
# Given a column title as appear in an Excel sheet, return its corresponding
# column number.
# 
# For example:
# 
# 
# ⁠   A -> 1
# ⁠   B -> 2
# ⁠   C -> 3
# ⁠   ...
# ⁠   Z -> 26
# ⁠   AA -> 27
# ⁠   AB -> 28 
# ⁠   ...
# 
# 
# Example 1:
# 
# 
# Input: "A"
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: "AB"
# Output: 28
# 
# 
# Example 3:
# 
# 
# Input: "ZY"
# Output: 701
# 
#
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return None

        l2n_dic = {chr(l):i+1 for i, l in enumerate(range(ord('A'), ord('A')+26))}

        ret = 0
        for i, c in enumerate(s[::-1]):
            ret+=26**i*l2n_dic[c]
        return ret
        
