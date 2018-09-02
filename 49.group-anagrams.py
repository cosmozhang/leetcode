#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams/description/
#
# algorithms
# Medium (40.40%)
# Total Accepted:    231.3K
# Total Submissions: 566.1K
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# Given an array of strings, group anagrams together.
# 
# Example:
# 
# 
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
# ⁠ ["ate","eat","tea"],
# ⁠ ["nat","tan"],
# ⁠ ["bat"]
# ]
# 
# Note:
# 
# 
# All inputs will be in lowercase.
# The order of your output does not matter.
# 
# 
#
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        count_dic = {}
        for word in strs:
            cnt_tb = [0 for i in range(26)]
            for char in word:
                char_code = ord(char)-ord('a')
                cnt_tb[char_code] += 1
            if tuple(cnt_tb) in count_dic:
                count_dic[tuple(cnt_tb)].append(word)
            else:
                count_dic[tuple(cnt_tb)] = [word]
        res = [v for (k, v) in count_dic.items()]
        return res
                
