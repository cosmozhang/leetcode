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
        
        first = digits[0]
        if first == '2': ab = ['a', 'b', 'c']
        if first == '3': ab = ['d', 'e', 'f']
        if first == '4': ab = ['g', 'h', 'i']
        if first == '5': ab = ['j', 'k', 'l']
        if first == '6': ab = ['m', 'n', 'o']
        if first == '7': ab = ['p', 'q', 'r', 's']
        if first == '8': ab = ['t', 'u', 'v']
        if first == '9': ab = ['w', 'x', 'y', 'z']
        
        if len(digits[1:]) > 0:
            new_ls =[]
            to_con = self.letterCombinations(digits[1:])
            for l in ab:
                for e in to_con:
                    new_ls.append(l+e)
            return new_ls
        else:
            return ab
                    
                
