#
# [79] Word Search
#
# https://leetcode.com/problems/word-search/description/
#
# algorithms
# Medium (28.66%)
# Total Accepted:    205.1K
# Total Submissions: 709.6K
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# Given a 2D board and a word, find if the word exists in the grid.
# 
# The word can be constructed from letters of sequentially adjacent cell, where
# "adjacent" cells are those horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
# 
# Example:
# 
# 
# board =
# [
# ⁠ ['A','B','C','E'],
# ⁠ ['S','F','C','S'],
# ⁠ ['A','D','E','E']
# ]
# 
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
# 
# 
#
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                if self.search(board, i, j, word):
                    return True

        return False

    def search(self, board, i, j, word):
        if not word:
            return True
        
        m = len(board)
        n = len(board[0])
        if i < 0 or i >= m or j < 0 or j >= n:
            return False
        
        if board[i][j] == word[0] and (i, j):
            temp = board[i][j]
            board[i][j] = None
            if self.search(board, i+1, j, word[1:]):
                return True
            elif self.search(board, i-1, j, word[1:]):
                return True
            elif self.search(board, i, j-1, word[1:]):
                return True
            elif self.search(board, i, j+1, word[1:]):
                return True
            board[i][j] = temp
            return False
        else:
            return False
        
