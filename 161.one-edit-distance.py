#
# [161] One Edit Distance
#
# https://leetcode.com/problems/one-edit-distance/description/
#
# algorithms
# Medium (31.31%)
# Total Accepted:    64.9K
# Total Submissions: 207.2K
# Testcase Example:  '"ab"\n"acb"'
#
# Given two strings s and t, determine if they are both one edit distance
# apart.
# 
# Note: 
# 
# There are 3 possiblities to satisify one edit distance apart:
# 
# 
# Insert a character into s to get t
# Delete a character from s to get t
# Replace a character of s to get t
# 
# 
# Example 1:
# 
# 
# Input: s = "ab", t = "acb"
# Output: true
# Explanation: We can insert 'c' into s to get t.
# 
# 
# Example 2:
# 
# 
# Input: s = "cab", t = "ad"
# Output: false
# Explanation: We cannot get t from s by only one step.
# 
# Example 3:
# 
# 
# Input: s = "1203", t = "1213"
# Output: true
# Explanation: We can replace '0' with '1' to get t.
# 
#
class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if abs(len(s) - len(t)) > 1:
            return False

        if len(s) == len(t):
            diff = 0
            for c1, c2 in zip(s, t):
                if c1!=c2:
                    diff += 1
                    if diff > 1:
                        return False
            if diff == 1:
                return True
            else:
                return False
        elif len(s) < len(t):
            if len(s) == 0:
                return True
            diff = 0
            idx_s, idx_t = 0, 0
            while idx_s < len(s):
                if s[idx_s] != t[idx_t]:
                    idx_t += 1
                    diff += 1
                    if diff > 1:
                        return False
                else:
                    idx_s += 1
                    idx_t += 1
            return True
        else:
            if len(t) ==0:
                return True
            diff = 0
            idx_s, idx_t =0, 0
            while idx_t < len(t):
                if s[idx_s] != t[idx_t]:
                    idx_s += 1
                    diff += 1
                    if diff > 1:
                        return False
                else:
                    idx_s += 1
                    idx_t += 1
            return True
