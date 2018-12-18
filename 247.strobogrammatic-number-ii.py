#
# [247] Strobogrammatic Number II
#
# https://leetcode.com/problems/strobogrammatic-number-ii/description/
#
# algorithms
# Medium (42.67%)
# Total Accepted:    39.7K
# Total Submissions: 92.7K
# Testcase Example:  '2'
#
# A strobogrammatic number is a number that looks the same when rotated 180
# degrees (looked at upside down).
# 
# Find all strobogrammatic numbers that are of length = n.
# 
# Example:
# 
# 
# Input:  n = 2
# Output: ["11","69","88","96"]
# 
# 
#
class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = self.inner(n, True)
        return ret

    def inner(self, n, most_out=False):
        if n == 0:
            return ['']
        elif n == 1:
            return ['0', '1', '8']
        else:
            ret_ls = []
            from_inner = self.inner(n-2)
            for ils in from_inner:
                ret_ls.append('6'+ils+'9')
                ret_ls.append('9'+ils+'6')
                ret_ls.append('8'+ils+'8')
                ret_ls.append('1'+ils+'1')
                if not most_out:
                    ret_ls.append('0'+ils+'0')
            return ret_ls
            
            
