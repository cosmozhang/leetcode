#
# [387] First Unique Character in a String
#
# https://leetcode.com/problems/first-unique-character-in-a-string/description/
#
# algorithms
# Easy (47.80%)
# Total Accepted:    183.8K
# Total Submissions: 384.5K
# Testcase Example:  '"leetcode"'
#
# 
# Given a string, find the first non-repeating character in it and return it's
# index. If it doesn't exist, return -1.
# 
# Examples:
# 
# s = "leetcode"
# return 0.
# 
# s = "loveleetcode",
# return 2.
# 
# 
# 
# 
# Note: You may assume the string contain only lowercase letters.
# 
#
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        s_ls = list(s)
        l_dict = {}
        for i, c in enumerate(s):
            if c not in l_dict:
                l_dict[c] = [i, 1]
            else:
                l_dict[c][1] += 1
        min_idx = float('inf')
        for k, v in l_dict.iteritems():
            if v[1] == 1:
                min_idx = min(min_idx, v[0])
        return min_idx if min_idx != float('inf') else -1
            
