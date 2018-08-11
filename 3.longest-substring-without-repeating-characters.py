#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (24.90%)
# Total Accepted:    543.1K
# Total Submissions: 2.2M
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
# 
# Examples:
# 
# Given "abcabcbb", the answer is "abc", which the length is 3.
# 
# Given "bbbbb", the answer is "b", with the length of 1.
# 
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the
# answer must be a substring, "pwke" is a subsequence and not a substring.
# 
#
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        else:
            '''
            len_dic = {}
            for gap in range(len(s)):
                for b in range(0, len(s) - gap):
                    e = b + gap
                    if b == e:
                        len_dic[(b, e)] = 1
                    else:
                        if (s[e] not in s[b:e]) and (len_dic[(b, e-1)] == len(s[b:e])):
                            len_dic[(b, e)] = len_dic[(b, e-1)] + 1
                        else:
                            len_dic[(b, e)] = len_dic[(b+1, e)] if len_dic[(b+1, e)] > len_dic[(b, e-1)] else len_dic[(b, e-1)]
            return len_dic[(0, len(s)-1)]
            '''
            span_start_idx = 0
            span_end_idx = 0
            cur_max_l = 1
            max_l = 1
            while span_end_idx < len(s)-1:
                span_end_idx += 1
                if s[span_end_idx] not in s[span_start_idx:span_end_idx]:
                    cur_max_l += 1
                    if cur_max_l > max_l:
                        max_l = cur_max_l
                else:
                    rep_pos = s[span_start_idx:span_end_idx].index(s[span_end_idx])
                    span_start_idx = span_start_idx + rep_pos + 1
                    cur_max_l = span_end_idx - span_start_idx + 1 
            return max_l
                
