# -*- coding: utf-8 -*-
# @Time    : 2019/1/9
# @Author  : qirui
# @FileName: 787. Cheapest Flights Within K Stops.py

import collections


# 27 / 41 test cases passed. Memory Limit Exceeded
# class Solution(object):
#     def findCheapestPrice(self, n, flights, src, dst, K):
#         """
#         :type n: int
#         :type flights: List[List[int]]
#         :type src: int
#         :type dst: int
#         :type K: int
#         :rtype: int
#         """
#
#         graph = collections.defaultdict(list)
#         for u, v, w in flights:
#             graph[u].append((v, w))
#
#         queue, depth, possible_cost = [(src, 0)], 0, []
#
#         while queue:
#             new_queue = []
#             depth += 1
#             if depth > K + 1:
#                 break
#             for city, total_cost in queue:
#                 for nei, cost in graph[city]:
#                     new_cost = total_cost + cost
#                     if nei == dst:
#                         possible_cost.append(new_cost)
#                     new_queue.append((nei, new_cost))
#             queue = new_queue
#
#         return min(possible_cost) if possible_cost else -1

# Time: O(N)
# Space: O(N)
# BFS with optimization
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """

        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        queue, depth, res = [(src, 0)], 0, float('inf')
        while queue:
            new_queue = []
            depth += 1
            if depth > K + 1:
                break
            for city, total_cost in queue:
                for nei, cost in graph[city]:
                    new_cost = total_cost + cost
                    if new_cost < res:
                        if nei == dst:
                            res = new_cost
                        new_queue.append((nei, new_cost))
            queue = new_queue
        return res if res!=float('inf') else -1


# Time: O(N)
# Space: O(N)
# DFS with memorization
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """

        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        memo = [[-1 for _ in range(K + 1)] for _ in range(n)]

        def dfs(v, k):
            if memo[v][k] != -1:
                return memo[v][k]
            if v == dst:
                return 0
            if k <= -1 or not graph[v]:
                return float('inf')
            memo[v][k] = min(cost + dfs(nei, k - 1) for nei, cost in graph[v])
            return memo[v][k]

        res = dfs(src, K)
        return res if res != float('inf') else -1


if __name__ == '__main__':
    S = Solution()
    n = 3
    edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 0

    print(S.findCheapestPrice(n, edges, src, dst, k))
