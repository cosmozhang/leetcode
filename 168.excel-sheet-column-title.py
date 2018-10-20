#
# [168] Excel Sheet Column Title
#
# https://leetcode.com/problems/excel-sheet-column-title/description/
#
# algorithms
# Easy (27.98%)
# Total Accepted:    152.4K
# Total Submissions: 544.3K
# Testcase Example:  '1'
#
# Given a positive integer, return its corresponding column title as appear in
# an Excel sheet.
# 
# For example:
# 
# 
# ⁠   1 -> A
# ⁠   2 -> B
# ⁠   3 -> C
# ⁠   ...
# ⁠   26 -> Z
# ⁠   27 -> AA
# ⁠   28 -> AB 
# ⁠   ...
# 
# 
# Example 1:
# 
# 
# Input: 1
# Output: "A"
# 
# 
# Example 2:
# 
# 
# Input: 28
# Output: "AB"
# 
# 
# Example 3:
# 
# 
# Input: 701
# Output: "ZY"
# 
#
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <1:
            return None
        ret_ls = []
        alp_dic = {i+1:chr(char) for i, char in enumerate(range(ord('A'), ord('A')+25))}
        alp_dic[0] = 'Z'
        while n != 0:
            s = n%26
            ret_ls.append(alp_dic[s])
            n = (n-s)/26 if s !=0 else (n-26)/26
        return ''.join(ret_ls)[::-1]
                
            
