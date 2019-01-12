# -*- coding: utf-8 -*-
# @Time    : 2019/1/9
# @Author  : qirui
# @FileName: 310. Minimum Height Trees.py

import collections


# 62 / 66 test cases passed.    Time Limit Exceeded
# class Solution(object):
#     def findMinHeightTrees(self, n, edges):
#         """
#         :type n: int
#         :type edges: List[List[int]]
#         :rtype: List[int]
#         """
#         graph = collections.defaultdict(list)
#         for edge in edges:
#             graph[edge[0]].append(edge[1])
#             graph[edge[1]].append(edge[0])
#
#         def get_height(v):
#             queue, visited, new_queue, res = [v], set(), [], 0
#             while queue:
#                 cur = queue.pop(0)
#                 visited.add(cur)
#                 for nei in graph[cur]:
#                     if nei not in visited:
#                         new_queue.append(nei)
#                 if not queue:
#                     queue = new_queue
#                     new_queue = []
#                     res += 1
#             return res
#
#         height_list = [get_height(v) for v in range(n)]
#         min_height = min(height_list)
#         return [i for i in range(n) if height_list[i] == min_height]

# Learn from discuss
# Time: O(N)
# Space: O(N)
# BFS + Graph
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        if n == 1:
            return [0]

        graph = collections.defaultdict(list)
        degree = collections.defaultdict(int)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1

        cur_level = [i for i in range(n) if degree[i] == 1]
        unvisited = set(range(n))
        while len(unvisited) > 2:
            next_level = []
            for v in cur_level:
                unvisited.remove(v)
                for nei in graph[v]:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        next_level.append(nei)
            cur_level = next_level
        return cur_level

# Learn from discuss
# Time: O(N)
# Space: O(N)
# BFS optimization
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        if n == 1:
            return [0]

        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        leaves = [i for i in range(n) if len(graph[i]) == 1]
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for v in leaves:
                nei = graph[v].pop()
                graph[nei].remove(v)
                if len(graph[nei]) == 1:
                    new_leaves.append(nei)
            leaves = new_leaves
        return leaves


if __name__ == '__main__':
    S = Solution()
    n = 6
    edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
    print(S.findMinHeightTrees(n, edges))
