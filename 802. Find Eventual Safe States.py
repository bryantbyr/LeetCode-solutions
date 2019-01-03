# -*- coding: utf-8 -*-
# @Time    : 2019/1/1
# @Author  : qirui
# @FileName: 802. Find Eventual Safe States.py

# Time Limit Exceeded
# class Solution:
#     def eventualSafeNodes(self, graph):
#         """
#         :type graph: List[List[int]]
#         :rtype: List[int]
#         """
#
#         def dfs(v):
#             if not graph[v]:
#                 return True
#             if v in seen:
#                 return False
#             seen.add(v)
#             for nei in graph[v]:
#                 if not dfs(nei):
#                     return False
#             seen.remove(v)
#             return True
#
#         res, seen = [], set()
#         for v in range(len(graph)):
#             if dfs(v):
#                 res.append(v)
#         return res

# Time Limit Exceeded
# class Solution:
#     def eventualSafeNodes(self, graph):
#         """
#         :type graph: List[List[int]]
#         :rtype: List[int]
#         """
#
#         def dfs(v):
#             if v in res:
#                 return True
#             if v in seen:
#                 unvalidated.append(v)
#                 return False
#             seen.add(v)
#             for nei in graph[v]:
#                 if not dfs(nei):
#                     return False
#             seen.remove(v)
#             res.append(v)
#             return True
#
#         res, unvalidated, seen = [], [], set()
#         for v in range(len(graph)):
#             if v not in res + unvalidated:
#                 dfs(v)
#         return sorted(res)

# # DFS
# class Solution:
#     def eventualSafeNodes(self, graph):
#         """
#         :type graph: List[List[int]]
#         :rtype: List[int]
#         """
#
#         def dfs(v):
#             if visited[v] == 1:
#                 return True
#             if v in seen:
#                 visited[v] = -1
#                 return False
#             seen.add(v)
#             for nei in graph[v]:
#                 if not dfs(nei):
#                     return False
#             seen.remove(v)
#             visited[v] = 1
#             return True
#
#         visited, seen = [0 for _ in range(len(graph))], set()
#         for v in range(len(graph)):
#             if visited[v] == 0:
#                 dfs(v)
#         return [item for item in range(len(graph)) if visited[item] == 1]

# Time: O(N)
# Space: O(N)
# DFS
class Solution:
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """

        def dfs(v):
            if visited[v] == 1:
                return True
            # if visited[v] == 2:
            #     visited[v] = -1
            #     return False
            if visited[v] == -1:
                return False
            elif visited[v] == 2:
                visited[v] = -1
                return False
            visited[v] = 2
            for nei in graph[v]:
                if not dfs(nei):
                    return False
            visited[v] = 1
            return True

        visited = [0 for _ in range(len(graph))]
        for v in range(len(graph)):
            if visited[v] == 0:
                dfs(v)

        return list(filter(lambda x: visited[x] == 1, range(len(graph))))
        # return [item for item in range(len(graph)) if visited[item] == 1]

import collections

# Time: O(N)
# Space: O(N)
# DFS optimized
class Solution:
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """

        # WHITE: not visited node; GRAY: safe node; BLACK: unsafe node; BLUE: visited node but not sure
        WHITE, GRAY, BLACK, BLUE = 0, 1, 2, 3

        colors = collections.defaultdict(int)

        def dfs(v):
            if colors[v] == BLACK:
                colors[v] = BLUE
                return False
            colors[v] = BLACK
            for nei in graph[v]:
                if colors[nei] == GRAY:
                    continue
                if colors[nei] == BLUE or not dfs(nei):
                    return False
            colors[v] = GRAY
            return True

        for v in range(len(graph)):
            if colors[v] == WHITE:
                dfs(v)

        return list(filter(lambda x: colors[x] == GRAY, range(len(graph))))
        # return [item for item in range(len(graph)) if visited[item] == 1]


if __name__ == '__main__':
    S = Solution()
    print(S.eventualSafeNodes([[1, 2], [2, 3], [5], [0], [5], [], []]))
