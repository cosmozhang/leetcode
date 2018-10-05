#
# [130] Surrounded Regions
#
# https://leetcode.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (20.82%)
# Total Accepted:    117K
# Total Submissions: 561K
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions
# surrounded by 'X'.
# 
# A region is captured by flipping all 'O's into 'X's in that surrounded
# region.
# 
# Example:
# 
# 
# X X X X
# X O O X
# X X O X
# X O X X
# 
# 
# After running your function, the board should be:
# 
# 
# X X X X
# X X X X
# X X X X
# X O X X
# 
# 
# Explanation:
# 
# Surrounded regions shouldn’t be on the border, which means that any 'O' on
# the border of the board are not flipped to 'X'. Any 'O' that is not on the
# border and it is not connected to an 'O' on the border will be flipped to
# 'X'. Two cells are connected if they are adjacent cells connected
# horizontally or vertically.
# 
#
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        if not board:
            return
        
        res_ls = []
        m, n = len(board), len(board[0])
        for i in range(m):
            if board[i][0] == 'O':
                self.helper(i, 0, board)
            if board[i][n-1] == 'O':
                self.helper(i, n-1, board)
                
        for j in range(n):
            if board[0][j] == 'O':
                self.helper(0, j, board)
            if board[m-1][j] == 'O':
                self.helper(m-1, j, board)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '*':
                    board[i][j] = 'O'


    def helper(self, i, j, board):

        m, n = len(board), len(board[0])
        board[i][j] = '*'
        q = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
        visited = set()
        while q:
            (u, v) = q.pop(0)
            if 0<=u and u<m and 0<=v and v<n:
                if (u, v) not in visited and board[u][v] == 'O':
                    board[u][v] = '*'
                    visited.add((u, v))
                    q.extend([(u+1, v), (u-1, v), (u, v+1), (u, v-1)])


