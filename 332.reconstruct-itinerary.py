#
# [332] Reconstruct Itinerary
#
# https://leetcode.com/problems/reconstruct-itinerary/description/
#
# algorithms
# Medium (30.12%)
# Total Accepted:    60.6K
# Total Submissions: 201.2K
# Testcase Example:  '[["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]'
#
# Given a list of airline tickets represented by pairs of departure and arrival
# airports [from, to], reconstruct the itinerary in order. All of the tickets
# belong to a man who departs from JFK. Thus, the itinerary must begin with
# JFK.
# 
# Note:
# 
# 
# If there are multiple valid itineraries, you should return the itinerary that
# has the smallest lexical order when read as a single string. For example, the
# itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# All airports are represented by three capital letters (IATA code).
# You may assume all tickets form at least one valid itinerary.
# 
# 
# Example 1:
# 
# 
# Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
# 
# 
# Example 2:
# 
# 
# Input:
# [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is
# ["JFK","SFO","ATL","JFK","ATL","SFO"].
# But it is larger in lexical order.
# 
# DFS, and this question needs to be reviewed.
#
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph_dic = {}

        for s, d in tickets:
            if s in graph_dic:
                graph_dic[s] += [d]
            else:
                graph_dic[s] = [d]

        for k, v in graph_dic.iteritems():
            graph_dic[k].sort()

        
        results = []

        flights = len(tickets)

        self.dfs_helper('JFK', graph_dic, results, 0, flights)

        return results[::-1]


    def dfs_helper(self, city, graph_dic, results, visited, flights):

        if visited == flights:
            results.append(city)
            return True

        if city in graph_dic:

            ncs = sorted(graph_dic[city])
            for nc in ncs:
                graph_dic[city].remove(nc)
                if not self.dfs_helper(nc, graph_dic, results, visited+1, flights):
                    graph_dic[city].append(nc)
                else:
                    results.append(city)
                    return True
            return False
        else:
            return False
                
                
        
