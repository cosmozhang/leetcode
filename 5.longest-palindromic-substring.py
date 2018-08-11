#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (25.63%)
# Total Accepted:    352.7K
# Total Submissions: 1.4M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
# 
# Example 1:
# 
# 
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: "cbbd"
# Output: "bb"
# 
# 
#
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if len(s) == 0:
            return ""
        elif len(s) == 1:
            return s
        elif len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        else:
            cur_l = 1
            max_l = 1
            max_s = s[0]
            # check even
            for m in range(1, len(s)):
                start_id = m -1
                end_id = m + 1
                while start_id >=0 and end_id <= len(s):
                    if s[start_id] == s[end_id-1]:
                        cur_l = end_id - start_id
                        if cur_l > max_l:
                            max_l = cur_l
                            max_s = s[start_id:end_id]
                        start_id -= 1
                        end_id += 1
                    else:
                        break
                            
            # check odd
            for m in range(1, len(s)-1):
                start_id = m - 1
                end_id = m + 1
                while start_id >=0 and end_id < len(s):
                    if s[start_id] == s[end_id]:
                        cur_l = end_id - start_id + 1
                        if cur_l > max_l:
                            max_l = cur_l
                            max_s = s[start_id:end_id+1]
                        start_id -= 1
                        end_id += 1
                    else:
                        break
                            
            return max_s
            
