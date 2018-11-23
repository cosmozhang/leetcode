#
# [211] Add and Search Word - Data structure design
#
# https://leetcode.com/problems/add-and-search-word-data-structure-design/description/
#
# algorithms
# Medium (27.83%)
# Total Accepted:    94.7K
# Total Submissions: 340K
# Testcase Example:  '["WordDictionary","addWord","addWord","addWord","search","search","search","search"]\n[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]'
#
# Design a data structure that supports the following two operations:
# 
# 
# void addWord(word)
# bool search(word)
# 
# 
# search(word) can search a literal word or a regular expression string
# containing only letters a-z or .. A . means it can represent any one letter.
# 
# Example:
# 
# 
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
# 
# 
# Note:
# You may assume that all words are consist of lowercase letters a-z.
# 
#
class TrieNode(object):

    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        if len(word) > 0:
            for c in word:
                if c in node.children:
                    node = node.children[c]
                else:
                    node.children[c] = TrieNode()
                    node = node.children[c]
            node.isWord = True
        
    def _find(self, node, w_ls):

        if len(w_ls) == 0 and node.isWord:
            return True
        elif len(w_ls) == 0 and not node.isWord:
            return False
        
        w = w_ls[0]
        if w in node.children:
            return self._find(node.children[w], w_ls[1:])
        elif w == '.':
            for child in node.children:
                if self._find(node.children[child], w_ls[1:]):
                    return True
            return False
        else:
            return False
                    
        
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if len(word) == 0:
            return True

        return self._find(self.root, word)
                    


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
