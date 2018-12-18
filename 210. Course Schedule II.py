# -*- coding: utf-8 -*-
# @Time    : 2018/12/18
# @Author  : qirui
# @FileName: 210. Course Schedule II.py

import collections


# Learn from Solution on 20181218
# Time:O(N)
# Space:O(N)
# DFS/Topological Sort + Graph
class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        def make_graph(adjEdges):
            graph = collections.defaultdict(list)
            for u, v in adjEdges:
                graph[v].append(u)
            return graph

        def dfs(v, visited, onpath):
            visited[v] = True
            onpath[v] = True
            for neighbor in graph[v]:
                if (not visited[neighbor] and dfs(neighbor, visited, onpath)) or (onpath[neighbor]):
                    return True

            topological_order.append(v)
            onpath[v] = False
            return False

        graph = make_graph(prerequisites)
        topological_order = []
        visited = [False] * numCourses
        onpath = [False] * numCourses
        for node in range(numCourses):
            if not visited[node]:
                if dfs(node, visited, onpath):
                    return []

        topological_order.reverse()
        return topological_order


if __name__ == '__main__':
    S = Solution()
    print(S.findOrder(2, [[1, 0], [0, 1]]))
