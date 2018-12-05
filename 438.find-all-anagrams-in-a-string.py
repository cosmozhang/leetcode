#
# [438] Find All Anagrams in a String
#
# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Easy (34.96%)
# Total Accepted:    89.4K
# Total Submissions: 255.6K
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# Given a string s and a non-empty string p, find all the start indices of p's
# anagrams in s.
# 
# Strings consists of lowercase English letters only and the length of both
# strings s and p will not be larger than 20,100.
# 
# The order of output does not matter.
# 
# Example 1:
# 
# Input:
# s: "cbaebabacd" p: "abc"
# 
# Output:
# [0, 6]
# 
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# 
# 
# 
# Example 2:
# 
# Input:
# s: "abab" p: "ab"
# 
# Output:
# [0, 1, 2]
# 
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
# 
# 
# sliding window propotype
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        '''
        wl = len(p)
        hash_ls = [0 for _ in range(26)]
        for c in p:
            hash_ls[ord(c)-ord('a')]+=1
                
        res_ls = []

        l, r = 0, 0
        cnt = len(p)
        while r < len(s):
            if hash_ls[ord(s[r]) - ord('a')]>0:
                cnt -= 1
            hash_ls[ord(s[r]) - ord('a')] -= 1
            r+=1

            if cnt == 0:
                res_ls +=[l]

            if r-l == len(p):
                if hash_ls[ord(s[l]) - ord('a')] >=0:
                    cnt += 1
                hash_ls[ord(s[l]) - ord('a')] += 1
                l += 1
            

        return res_ls
        '''

        if len(s) < len(p):
            return []

        p_dic = {}
        for c in p:
            if c in p_dic:
                p_dic[c] += 1
            else:
                p_dic[c] = 1

        s_dic = {}
        l = 0
        r = len(p) - 1

        for i in range(len(p)):
            c = s[i]
            if c in s_dic:
                s_dic[c] += 1
            elif c in p_dic:
                s_dic[c] = 1
                
        ret_ls = []
        if self.isAnagram(p_dic, s_dic):
            ret_ls.append(0)
        while True:
            old_l = s[l]
            if old_l in s_dic:
                s_dic[old_l] -= 1
            l += 1
            r += 1
            if r == len(s):
                break
            new_r = s[r]
            if new_r in s_dic:
                s_dic[new_r] += 1
            elif new_r in p_dic:
                s_dic[new_r] = 1
            if self.isAnagram(p_dic, s_dic):
                ret_ls.append(l)

        return ret_ls

    def isAnagram(self, p_dic, s_dic):

        for k, v in p_dic.iteritems():
            if k not in s_dic or v != s_dic[k]:
                return False
        return True
