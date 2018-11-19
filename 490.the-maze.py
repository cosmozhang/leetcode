#
# [490] The Maze
#
# https://leetcode.com/problems/the-maze/description/
#
# algorithms
# Medium (45.07%)
# Total Accepted:    23.8K
# Total Submissions: 52.7K
# Testcase Example:  '[[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]\n[0,4]\n[4,4]'
#
# There is a ball in a maze with empty spaces and walls. The ball can go
# through empty spaces by rolling up, down, left or right, but it won't stop
# rolling until hitting a wall. When the ball stops, it could choose the next
# direction.
# 
# Given the ball's start position, the destination and the maze, determine
# whether the ball could stop at the destination.
# 
# The maze is represented by a binary 2D array. 1 means the wall and 0 means
# the empty space. You may assume that the borders of the maze are all walls.
# The start and destination coordinates are represented by row and column
# indexes.
# 
# 
# 
# Example 1:
# 
# 
# Input 1: a maze represented by a 2D array
# 
# 0 0 1 0 0
# 0 0 0 0 0
# 0 0 0 1 0
# 1 1 0 1 1
# 0 0 0 0 0
# 
# Input 2: start coordinate (rowStart, colStart) = (0, 4)
# Input 3: destination coordinate (rowDest, colDest) = (4, 4)
# 
# Output: true
# 
# Explanation: One possible way is : left -> down -> left -> down -> right ->
# down -> right.
# 
# 
# 
# Example 2:
# 
# 
# Input 1: a maze represented by a 2D array
# 
# 0 0 1 0 0
# 0 0 0 0 0
# 0 0 0 1 0
# 1 1 0 1 1
# 0 0 0 0 0
# 
# Input 2: start coordinate (rowStart, colStart) = (0, 4)
# Input 3: destination coordinate (rowDest, colDest) = (3, 2)
# 
# Output: false
# 
# Explanation: There is no way for the ball to stop at the destination.
# 
# 
# 
# 
# 
# Note:
# 
# 
# There is only one ball and one destination in the maze.
# Both the ball and the destination exist on an empty space, and they will not
# be at the same position initially.
# The given maze does not contain border (like the red rectangle in the example
# pictures), but you could assume the border of the maze are all walls.
# The maze contains at least 2 empty spaces, and both the width and height of
# the maze won't exceed 100.
# 
# 
#
class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        m, n = len(maze), len(maze[0])
        return self.helper(maze, m, n, start, destination, (-1, 0)) or self.helper(maze, m, n, start, destination, (1, 0)) or self.helper(maze, m, n, start, destination, (0, -1)) or self.helper(maze, m, n, start, destination, (0, 1))
    
    def helper(self, maze, m, n, (s0, s1), (d0, d1), direc):

        xp, yp = direc
        if s0 + xp < 0 or s0+xp > m-1 or s1+yp < 0 or s1+yp > n-1 or maze[s0+xp][s1+yp] == 1:
            return False
        else:
            while s0+xp>=0 and s0+xp<=m-1 and s1+yp>=0 and s1+yp<=n-1 and maze[s0+xp][s1+yp] != 1:
                s0 += xp
                s1 += yp

            if maze[s0][s1] == 'X':
                return False
            else:
                maze[s0][s1] = 'X'
                if s0 == d0 and s1 == d1:
                    return True
                else:
                    return self.helper(maze, m, n, (s0, s1), (d0, d1), (-1, 0)) or self.helper(maze, m, n, (s0, s1), (d0, d1), (1, 0)) or self.helper(maze, m, n, (s0, s1), (d0, d1), (0, 1)) or self.helper(maze, m, n, (s0, s1), (d0, d1), (0, -1))
        
