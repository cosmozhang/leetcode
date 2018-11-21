#
# [778] Reorganize String
#
# https://leetcode.com/problems/reorganize-string/description/
#
# algorithms
# Medium (39.83%)
# Total Accepted:    15.7K
# Total Submissions: 39.3K
# Testcase Example:  '"aab"'
#
# Given a string S, check if the letters can be rearranged so that two
# characters that are adjacent to each other are not the same.
# 
# If possible, output any possible result.  If not possible, return the empty
# string.
# 
# Example 1:
# 
# 
# Input: S = "aab"
# Output: "aba"
# 
# 
# Example 2:
# 
# 
# Input: S = "aaab"
# Output: ""
# 
# 
# Note:
# 
# 
# S will consist of lowercase letters and have length in range [1, 500].
# 
# 
# 
# 
#
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        
        buckets = [[] for _ in range(26)]

        b = ord('a')
        for c in S:
            buckets[ord(c) - b].append(c)

        max_v = 0
        for idx, bucket in enumerate(buckets):
            t = len(bucket)
            if t > max_v:
                max_v = t
                b_idx = idx
        ret = ''
        if max_v > (1+len(S))/2:
            return ret
        else:
            temp_ls = [None for _ in range(len(S))]
            b_bucket = buckets.pop(b_idx)
            buckets.append(b_bucket)
            chained = reduce(lambda x, y: x+y, buckets)
            idx = 1
            while len(chained) > 0:
                c = chained.pop(0)
                temp_ls[idx] = c
                idx+=2
                if idx >= len(S):
                    idx = 0
            ret = ''.join(temp_ls)
            return ret
            
