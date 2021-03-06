#
# [807] Custom Sort String
#
# https://leetcode.com/problems/custom-sort-string/description/
#
# algorithms
# Medium (59.63%)
# Total Accepted:    21.6K
# Total Submissions: 36.2K
# Testcase Example:  '"cba"\n"abcd"'
#
# S and T are strings composed of lowercase letters. In S, no letter occurs
# more than once.
# 
# S was sorted in some custom order previously. We want to permute the
# characters of T so that they match the order that S was sorted. More
# specifically, if x occurs before y in S, then x should occur before y in the
# returned string.
# 
# Return any permutation of T (as a string) that satisfies this property.
# 
# 
# Example :
# Input: 
# S = "cba"
# T = "abcd"
# Output: "cbad"
# Explanation: 
# "a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b",
# and "a". 
# Since "d" does not appear in S, it can be at any position in T. "dcba",
# "cdba", "cbda" are also valid outputs.
# 
# 
# 
# 
# Note:
# 
# 
# S has length at most 26, and no character is repeated in S.
# T has length at most 200.
# S and T consist of lowercase letters only.
# 
# need to care the situation when the char is not in the hashmap
#
class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        '''
        s_dic = {}
        for i, c in enumerate(S):
            s_dic[c]=i

        def cus_cmp(c1, c2):
            return s_dic.get(c1, 0) - s_dic.get(c2, 0)

        return ''.join(sorted(list(T), cmp=cus_cmp))
        '''

        c2p = {}

        for idx, c in enumerate(S):
            c2p[c] = idx+1

        for c in T:
            if c not in c2p:
                c2p[c] = 0

        def cuscomp(x, y):
            return c2p[x] - c2p[y]

        return ''.join(sorted(list(T), cmp=cuscomp))
