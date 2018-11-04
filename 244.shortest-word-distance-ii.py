#
# [244] Shortest Word Distance II
#
# https://leetcode.com/problems/shortest-word-distance-ii/description/
#
# algorithms
# Medium (43.88%)
# Total Accepted:    38.3K
# Total Submissions: 87.2K
# Testcase Example:  '["WordDistance","shortest","shortest"]\n[[["practice","makes","perfect","coding","makes"]],["coding","practice"],["makes","coding"]]'
#
# Design a class which receives a list of words in the constructor, and
# implements a method that takes two words word1 and word2 and return the
# shortest distance between these two words in the list. Your method will be
# called repeatedly many times with different parameters. 
# 
# Example:
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
# 
# 
# Input: word1 = “coding”, word2 = “practice”
# Output: 3
# 
# 
# 
# Input: word1 = "makes", word2 = "coding"
# Output: 1
# 
# Note:
# You may assume that word1 does not equal to word2, and word1 and word2 are
# both in the list.
# 
#
class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.dis_dic = {}
        for i in range(len(words)):
            c = words[i]
            if c not in self.dis_dic:
                self.dis_dic[c] = [i]
            else:
                self.dis_dic[c].append(i)

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        ls1 = self.dis_dic[word1]
        ls2 = self.dis_dic[word2]
        l = 0
        r = 0
        min_v = float('inf')
        while l < len(ls1) and r < len(ls2):
            c_v = abs(ls1[l] - ls2[r])
            if c_v < min_v:
                min_v = c_v
            if ls1[l] < ls2[r]:
                l += 1
            else:
                r += 1
        
        return min_v
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
