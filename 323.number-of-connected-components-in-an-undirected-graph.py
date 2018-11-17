#
# [323] Number of Connected Components in an Undirected Graph
#
# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/
#
# algorithms
# Medium (50.22%)
# Total Accepted:    47.8K
# Total Submissions: 95.2K
# Testcase Example:  '5\n[[0,1],[1,2],[3,4]]'
#
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each
# edge is a pair of nodes), write a function to find the number of connected
# components in an undirected graph.
# 
# Example 1:
# 
# 
# Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]
# 
# ⁠    0          3
# ⁠    |          |
# ⁠    1 --- 2    4 
# 
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
# 
# ⁠    0           4
# ⁠    |           |
# ⁠    1 --- 2 --- 3
# 
# Output:  1
# 
# 
# Note:
# You can assume that no duplicate edges will appear in edges. Since all edges
# are undirected, [0, 1] is the same as [1, 0] and thus will not appear
# together in edges.
# 
#
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        
        visited = set()
        cnt = 0
        linked_ls_dic = {i:[] for i in range(n)}
        for t in edges:
            linked_ls_dic[t[0]] += [t[1]]
            linked_ls_dic[t[1]] += [t[0]]

        for node in range(n):
            if node in visited:
                continue
            q = [node]
            while len(q) > 0:
                n = q.pop(0)
                for nbor in linked_ls_dic[n]:
                    if nbor not in visited:
                        q.append(nbor)
                        visited.add(nbor)
            cnt += 1

        return cnt
                    
                
                
        
