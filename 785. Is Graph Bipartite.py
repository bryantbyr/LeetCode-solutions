# -*- coding: utf-8 -*-
# @Time    : 2019/1/1
# @Author  : qirui
# @FileName: 785. Is Graph Bipartite.py

# Time:O(N)
# Space:O(N)
# DFS
class Solution:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """

        def dfs(cur_v, pre_v=-1):
            if (pre_v, cur_v) in seen_edge or (cur_v, pre_v) in seen_edge:
                return
            seen_edge.add((pre_v, cur_v))
            seen_node.add(cur_v)
            if pre_v == -1 or pre_v in set_2:
                set_1.add(cur_v)
            elif pre_v in set_1:
                set_2.add(cur_v)

            for nei in graph[cur_v]:
                dfs(nei, cur_v)

        set_1, set_2 = set(), set()
        seen_edge, seen_node = set(), set()
        for i in range(len(graph)):
            if i not in seen_node:
                dfs(i)

        return True if not set_1.intersection(set_2) else False

# Time:O(N)
# Space:O(N)
# DFS optimized using returned value
class Solution:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """

        def dfs(cur_v, index):
            if cur_v in set[index]:
                return True
            elif cur_v in set[1 - index]:
                return False
            set[index].append(cur_v)
            for nei in graph[cur_v]:
                if not dfs(nei, 1 - index):
                    return False
            return True

        set = [list(), list()]
        for i in range(len(graph)):
            if i not in set[0] + set[1] and not dfs(i, 0):
                    return False

        return True


# Time:O(N)
# Space:O(N)
# DFS (m Coloring Problem)
class Solution:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """

        def dfs(v, color):
            if colors[v] != 0:
                return colors[v] == color
            colors[v] = color
            for nei in graph[v]:
                if not dfs(nei, -color):
                    return False
            return True

        colors = [0 for _ in range(len(graph))]
        for i in range(len(graph)):
            if colors[i] == 0 and not dfs(i, 1):
                return False
        return True


# Time:O(2^N)
# Space:O(N)
# DFS/Recursion using vertex number
# Time Limit Exceeded
# class Solution:
#     def isBipartite(self, graph):
#         """
#         :type graph: List[List[int]]
#         :rtype: bool
#         """

#         def isvalid(v, c):
#             for nei in graph[v]:
#                 if colors[nei] == c:
#                     return False
#             return True

#         def dfs(v):
#             if v == vertices:
#                 return True
#             for c in [1, -1]:
#                 if isvalid(v, c):
#                     colors[v] = c
#                     if dfs(v + 1):
#                         return True
#                     colors[v] = 0
#             return False

#         vertices = len(graph)
#         colors = [0 for _ in range(vertices)]
#         return dfs(0)

# Time:O(2^N)
# Space:O(N)
# BFS
class Solution:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """

        colors = [0 for _ in range(len(graph))]

        for v in range(len(graph)):
            if colors[v] == 0:
                queue, colors[v] = [v], 1
                while queue:
                    node = queue.pop(0)
                    for nei in graph[node]:
                        if colors[nei] != 0:
                            if colors[nei] == -colors[node]:
                                continue
                            else:
                                return False
                        queue.append(nei)
                        colors[nei] = -colors[node]
        return True


if __name__ == '__main__':
    S = Solution()
    print(S.isBipartite(
        [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))
