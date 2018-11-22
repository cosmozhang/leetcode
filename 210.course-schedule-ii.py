#
# [210] Course Schedule II
#
# https://leetcode.com/problems/course-schedule-ii/description/
#
# algorithms
# Medium (32.35%)
# Total Accepted:    115.7K
# Total Submissions: 357.7K
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of n courses you have to take, labeled from 0 to n-1.
# 
# Some courses may have prerequisites, for example to take course 0 you have to
# first take course 1, which is expressed as a pair: [0,1]
# 
# Given the total number of courses and a list of prerequisite pairs, return
# the ordering of courses you should take to finish all courses.
# 
# There may be multiple correct orders, you just need to return one of them. If
# it is impossible to finish all courses, return an empty array.
# 
# Example 1:
# 
# 
# Input: 2, [[1,0]] 
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you
# should have finished   
# course 0. So the correct course order is [0,1] .
# 
# Example 2:
# 
# 
# Input: 4, [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,1,2,3] or [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you
# should have finished both     
# ⁠            courses 1 and 2. Both courses 1 and 2 should be taken after you
# finished course 0. 
# So one correct course order is [0,1,2,3]. Another correct ordering is
# [0,2,1,3] .
# 
# Note:
# 
# 
# The input prerequisites is a graph represented by a list of edges, not
# adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.
# 
# 
#
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        graph_dic = {}
        for u, v in prerequisites:
            if v not in graph_dic:
                graph_dic[v] = [u]
            else:
                graph_dic[v] += [u]

        states = [0 for _ in range(numCourses)]

        ret_stack = []
        
        for c in range(numCourses):
            res = self.helper(graph_dic, states, ret_stack, c)
            if not res:
                return []

        return ret_stack[::-1]
        

    def helper(self, graph_dic, states, ret_stack, node):
        if states[node] == 1:
            return False
        if states[node] == 2:
            return True

        states[node] = 1
        if node in graph_dic:
            for n in graph_dic[node]:
                if not self.helper(graph_dic, states, ret_stack, n):
                    return False
        states[node] = 2

        ret_stack.append(node)
        return True

        
