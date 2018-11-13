#
# [874] Backspace String Compare
#
# https://leetcode.com/problems/backspace-string-compare/description/
#
# algorithms
# Easy (43.32%)
# Total Accepted:    26.4K
# Total Submissions: 61K
# Testcase Example:  '"ab#c"\n"ad#c"'
#
# Given two strings S and T, return if they are equal when both are typed into
# empty text editors. # means a backspace character.
# 
# 
# Example 1:
# 
# 
# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".
# 
# 
# 
# Example 2:
# 
# 
# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".
# 
# 
# 
# Example 3:
# 
# 
# Input: S = "a##c", T = "#a#c"
# Output: true
# Explanation: Both S and T become "c".
# 
# 
# 
# Example 4:
# 
# 
# Input: S = "a#c", T = "b"
# Output: false
# Explanation: S becomes "c" while T becomes "b".
# 
# 
# Note:
# 
# 
# 1 <= S.length <= 200
# 1 <= T.length <= 200
# S and T only contain lowercase letters and '#' characters.
# 
# 
# Follow up:
# 
# 
# Can you solve it in O(N) time and O(1) space?
# 
# 
# 
# 
# 
# 
#
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        
        # o(1) space

        i, j = len(S)-1, len(T)-1
        bsc, btc = 0, 0

        while i >= 0 or j >= 0:
            while i >= 0:
                # find next non '#'
                if S[i] == '#':
                    bsc += 1
                elif bsc > 0:
                    bsc -= 1
                else:
                    break
                i -= 1
            while j >= 0:
                if T[j] == '#':
                    btc += 1
                elif btc >0:
                    btc -= 1
                else:
                    break
                j -= 1
            if (i>=0 and j>=0) and S[i] != T[j]:
                return False
            if (i>=0 and j <0) or (i<0 and j >=0):
                return False
            i -= 1
            j -= 1
        return True
