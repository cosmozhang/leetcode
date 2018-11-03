#
# [768] Partition Labels
#
# https://leetcode.com/problems/partition-labels/description/
#
# algorithms
# Medium (65.84%)
# Total Accepted:    26.8K
# Total Submissions: 40.8K
# Testcase Example:  '"ababcbacadefegdehijhklij"'
#
# 
# A string S of lowercase letters is given.  We want to partition this string
# into as many parts as possible so that each letter appears in at most one
# part, and return a list of integers representing the size of these parts.
# 
# 
# Example 1:
# 
# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it
# splits S into less parts.
# 
# 
# 
# Note:
# S will have length in range [1, 500].
# S will consist of lowercase letters ('a' to 'z') only.
# 
#
class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        if not S:
            return []
        
        ret_ls = []
        pos_dic = {}
        for i, c in enumerate(S):
            pos_dic[c] = i
        s = 0
        max_v = 0
        for i, c in enumerate(S):
            if pos_dic[c] > max_v:
                max_v = pos_dic[c]
            elif i == max_v:
                ret_ls.append(S[s:i+1])
                s = i+1
                max_v = s
        return [len(l) for l in ret_ls]

'''
if __name__ == '__main__':
    s = Solution()
    s.partitionLabels("ababcbacadefegdehijhklij")
'''
