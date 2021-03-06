#
# [803] Cheapest Flights Within K Stops
#
# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/
#
# algorithms
# Medium (31.63%)
# Total Accepted:    21.4K
# Total Submissions: 67.7K
# Testcase Example:  '3\n[[0,1,100],[1,2,100],[0,2,500]]\n0\n2\n1'
#
# There are n cities connected by m flights. Each fight starts from city u and
# arrives at v with a price w.
# 
# Now given all the cities and flights, together with starting city src and the
# destination dst, your task is to find the cheapest price from src to dst with
# up to k stops. If there is no such route, output -1.
# 
# 
# Example 1:
# Input: 
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 1
# Output: 200
# Explanation: 
# The graph looks like this:
# 
# 
# The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as
# marked red in the picture.
# 
# 
# Example 2:
# Input: 
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 0
# Output: 500
# Explanation: 
# The graph looks like this:
# 
# 
# The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as
# marked blue in the picture.
# 
# Note:
# 
# 
# The number of nodes n will be in range [1, 100], with nodes labeled from 0 to
# n - 1.
# The size of flights will be in range [0, n * (n - 1) / 2].
# The format of each flight will be (src, dst, price).
# The price of each flight will be in the range [1, 10000].
# k is in the range of [0, n - 1].
# There will not be any duplicated flights or self cycles.
# 
# 
#
class Solution(object):
    '''
    # DFS solution
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """

        
        
        graph_dic = {}
        visiting = [0 for _ in range(n)]
        for s, d, p in flights:
            if s in graph_dic:
                graph_dic[s] += [(d, p)]
            else:
                graph_dic[s] = [(d, p)]
        best_price = [float('inf')]
        
        self.dfs(graph_dic, src, dst, visiting, K, 0, best_price)
        if best_price[-1] == float('inf'):
            return -1
        else:
            return best_price[-1]


    def dfs(self, graph_dic, new_src, dst, visiting, k, total_price, best_price):
        if new_src == dst:
            if total_price < best_price[-1]:
                best_price.append(total_price)
            return
        if k < 0:
            return

        if new_src in graph_dic:
            for new_dst, price in graph_dic[new_src]:
                if visiting[new_dst] == 1 or total_price + price > best_price[-1]:
                    continue
                visiting[new_dst] = 1
                self.dfs(graph_dic, new_dst, dst, visiting, k-1, total_price + price, best_price)
                visiting[new_dst] = 0
        return
    '''

    # BFS
    def findCheapestPrice(self, n, flights, src, dst, K):



        graph_dic = {}
        for s, d, p in flights:
            if s not in graph_dic:
                graph_dic[s] = [(d, p)]
            else:
                graph_dic[s] += [(d, p)]
        best_price = float('inf')
        k = -1
        q = [(src, 0)]

        while len(q) >0 :
            new_q = []
            
            for city, total_price in q:
                if city == dst:
                    best_price = min(total_price, best_price)
                if city in graph_dic:
                    for nc, price in graph_dic[city]:
                        if total_price + price < best_price:
                            new_q.append((nc, total_price + price))
            k+= 1
            if k > K:
                break
            q = new_q

        if best_price == float('inf'):
            return -1
        else:
            return best_price
                
        
