#
# [720] Longest Word in Dictionary
#
# https://leetcode.com/problems/longest-word-in-dictionary/description/
#
# algorithms
# Easy (42.68%)
# Total Accepted:    25.2K
# Total Submissions: 59K
# Testcase Example:  '["w","wo","wor","worl","world"]'
#
# Given a list of strings words representing an English Dictionary, find the
# longest word in words that can be built one character at a time by other
# words in words.  If there is more than one possible answer, return the
# longest word with the smallest lexicographical order.  If there is no answer,
# return the empty string.
# 
# Example 1:
# 
# Input: 
# words = ["w","wo","wor","worl", "world"]
# Output: "world"
# Explanation: 
# The word "world" can be built one character at a time by "w", "wo", "wor",
# and "worl".
# 
# 
# 
# Example 2:
# 
# Input: 
# words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
# Output: "apple"
# Explanation: 
# Both "apply" and "apple" can be built from other words in the dictionary.
# However, "apple" is lexicographically smaller than "apply".
# 
# 
# 
# Note:
# All the strings in the input will only contain lowercase letters.
# The length of words will be in the range [1, 1000].
# The length of words[i] will be in the range [1, 30].
# 
#

class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.isWord = False

class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        root = TrieNode()
        
        for word in words:
            
            self.addWord(root, word)


        if len(root.children) == 0:
            return ''

        lword = self.findLongestWord(root)

        return lword

    def addWord(self, root, word):

        word_ls = list(word)
        node = root
        while len(word_ls) > 0:

            c = word_ls.pop(0)

            if c not in node.children:
                node.children[c] = TrieNode()

            node = node.children[c]

        node.isWord = True

    def findLongestWord(self, node):


        lngest_word = ''

        for c, n in node.children.iteritems():
            if n.isWord:
                found_word = c + self.findLongestWord(n)
                if len(found_word) > len(lngest_word):
                    lngest_word = found_word
                elif len(found_word) == len(lngest_word):
                    lngest_word = min([found_word, lngest_word])
        return lngest_word
            
