#
# [408] Valid Word Abbreviation
#
# https://leetcode.com/problems/valid-word-abbreviation/description/
#
# algorithms
# Easy (28.63%)
# Total Accepted:    19.6K
# Total Submissions: 68.6K
# Testcase Example:  '"internationalization"\n"i12iz4n"'
#
# 
# Given a non-empty string s and an abbreviation abbr, return whether the
# string matches with the given abbreviation.
# 
# 
# A string such as "word" contains only the following valid abbreviations:
# 
# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1",
# "w1r1", "1o2", "2r1", "3d", "w3", "4"]
# 
# 
# Notice that only the above abbreviations are valid abbreviations of the
# string "word". Any other string is not a valid abbreviation of "word".
# 
# Note:
# Assume s contains only lowercase letters and abbr contains only lowercase
# letters and digits.
# 
# 
# Example 1:
# 
# Given s = "internationalization", abbr = "i12iz4n":
# 
# Return true.
# 
# 
# 
# Example 2:
# 
# Given s = "apple", abbr = "a2e":
# 
# Return false.
# 
# 
#
class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        nums = [str(i) for i in range(10)]
        
        w = ''
        s = ''
        for c in abbr:
            if c in nums:
                s += c
                if s == '0':
                    return False
                if int(s) > len(word):
                    return False
            else:
                if len(s) != 0:
                    f = int(s) * '+'
                    s = ''
                    w += f
                w += c
        if len(s) != 0:
            f = int(s)*'+'
            w += f
            s = ''

        if len(w) != len(word):
            return False
        else:
            for i, c in enumerate(w):
                if c != '+':
                    if word[i] != c:
                        return False
        return True
