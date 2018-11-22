#
# [207] Course Schedule
#
# https://leetcode.com/problems/course-schedule/description/
#
# algorithms
# Medium (35.43%)
# Total Accepted:    163.3K
# Total Submissions: 461K
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of n courses you have to take, labeled from 0 to n-1.
# 
# Some courses may have prerequisites, for example to take course 0 you have to
# first take course 1, which is expressed as a pair: [0,1]
# 
# Given the total number of courses and a list of prerequisite pairs, is it
# possible for you to finish all courses?
# 
# Example 1:
# 
# 
# Input: 2, [[1,0]] 
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# 
# Example 2:
# 
# 
# Input: 2, [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you
# should
# also have finished course 1. So it is impossible.
# 
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
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph_dic = {}

        for (n, c) in prerequisites:
            if c not in graph_dic:
                graph_dic[c] = [n]
            else:
                graph_dic[c] += [n]

        states = [0 for _ in range(numCourses)]

        for course in range(numCourses):
            if course in graph_dic:
                if not self.helper(graph_dic, course, states):
                    return False
        
        return True

    def helper(self, graph_dic, c, states):
        if states[c] == 1:
            return False
        if states[c] == 2:
            return True

        states[c] = 1
        for n in graph_dic[c]:
            if n in graph_dic:
                if not self.helper(graph_dic, n, states):
                    return False
        states[c] = 2
        
        return True
                        
                    
