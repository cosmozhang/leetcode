#
# [261] Graph Valid Tree
#
# https://leetcode.com/problems/graph-valid-tree/description/
#
# algorithms
# Medium (38.98%)
# Total Accepted:    73K
# Total Submissions: 187.3K
# Testcase Example:  '5\n[[0,1],[0,2],[0,3],[1,4]]'
#
# Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge
# is a pair of nodes), write a function to check whether these edges make up a
# valid tree.
# 
# Example 1:
# 
# 
# Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
# Output: true
# 
# Example 2:
# 
# 
# Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
# Output: false
# 
# Note: you can assume that no duplicate edges will appear in edges. Since all
# edges are undirected, [0,1] is the same as [1,0] and thus will not appear
# together in edges.
# 
#
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) == 0 and n == 1:
            return True
        
        visited = set([0])
        l_ls_dic = {}
        for (u, v) in edges:
            if u not in l_ls_dic:
                l_ls_dic[u] = [v]
            else:
                l_ls_dic[u] += [v]

            if v not in l_ls_dic:
                l_ls_dic[v] = [u]
            else:
                l_ls_dic[v] += [u]
        
        q = [(0, None)]
        while q:
            node, np = q.pop(0)
            if node not in l_ls_dic:
                return False
            for nbr in l_ls_dic[node]:
                if nbr != np:
                    if nbr in visited:
                        return False
                    else:
                        visited.add(nbr)
                        q.append((nbr, node))

        if len(visited) < n:
            return False
        else:
            return True

        
