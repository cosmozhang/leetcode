#
# [286] Walls and Gates
#
# https://leetcode.com/problems/walls-and-gates/description/
#
# algorithms
# Medium (47.14%)
# Total Accepted:    59.7K
# Total Submissions: 126.6K
# Testcase Example:  '[[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]'
#
# You are given a m x n 2D grid initialized with these three possible
# values.
# 
# 
# -1 - A wall or an obstacle.
# 0 - A gate.
# INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to
# represent INF as you may assume that the distance to a gate is less than
# 2147483647.
# 
# 
# Fill each empty room with the distance to its nearest gate. If it is
# impossible to reach a gate, it should be filled with INF.
# 
# Example: 
# 
# Given the 2D grid:
# 
# 
# INF  -1  0  INF
# INF INF INF  -1
# INF  -1 INF  -1
# ⁠ 0  -1 INF INF
# 
# 
# After running your function, the 2D grid should be:
# 
# 
# ⁠ 3  -1   0   1
# ⁠ 2   2   1  -1
# ⁠ 1  -1   2  -1
# ⁠ 0  -1   3   4
# 
# Find room instead of gates!
#
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if len(rooms) < 1 or len(rooms[0]) < 1:
            return
        
        m, n = len(rooms), len(rooms[0])

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        q = []
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i, j))

        while len(q) > 0:
            (i, j) = q.pop(0)
            for (u, v) in dirs:
                r = i + u
                s = j + v
                if r < 0 or r > m-1 or s < 0 or s > n-1 or rooms[r][s] == -1 or rooms[r][s] < rooms[i][j]+1:
                    continue
                else:
                    rooms[r][s] = rooms[i][j]+1
                    q.append((r, s))
                


                
