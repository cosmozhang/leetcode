#
# [17] Letter Combinations of a Phone Number
#
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (37.61%)
# Total Accepted:    264.9K
# Total Submissions: 703.1K
# Testcase Example:  '"23"'
#
# Given a string containing digits from 2-9 inclusive, return all possible
# letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given
# below. Note that 1 does not map to any letters.
#
#
#
# Example:
#
#
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#
#
# Note:
#
# Although the above answer is in lexicographical order, your answer could be
# in any order you want.
#
#
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []

        d2l_dic = {}
        d2l_dic['2'] = ['a', 'b', 'c']
        d2l_dic['3'] = ['d', 'e', 'f']
        d2l_dic['4'] = ['g', 'h', 'i']
        d2l_dic['5'] = ['j', 'k', 'l']
        d2l_dic['6'] = ['m', 'n', 'o']
        d2l_dic['7'] = ['p', 'q', 'r', 's']
        d2l_dic['8'] = ['t', 'u', 'v']
        d2l_dic['9'] = ['w', 'x', 'y', 'z']

        ret_ls = self.helper(digits, d2l_dic)
        return ret_ls

    def helper(self, digits, d2l_dic):
        if len(digits) == 0:
            return ['']

        letters = d2l_dic[digits[0]]
        temps = self.helper(digits[1:], d2l_dic)

        new_ls = []
        for l in letters:
            for s in temps:
                new_ls.append(l+s)

        return new_ls


