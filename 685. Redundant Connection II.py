# 685. Redundant Connection II

import collections


# 只判断了两种情况, 没考虑有环既有入度为2节点的情况
# class Solution:
#     def findRedundantDirectedConnection(self, edges):
#         """
#         :type edges: List[List[int]]
#         :rtype: List[int]
#         """
#
#         graph = collections.defaultdict(set)
#         set_target = set()
#
#         def dfs(source, target):
#             if source not in seen:
#                 seen.add(source)
#                 if source == target:
#                     return True
#                 return any(dfs(nei, target) for nei in graph[source])
#
#         for u, v in edges:
#             seen = set()
#             if v in set_target or (v in graph and dfs(v, u)):
#                 return (u, v)
#             graph[u].add(v)
#             set_target.add(v)

#Learn from discuss on 20181124
#Time:O(N^2)
#Space:O(N)
#Tree + DFS (注意考虑多种情况及其处理策略*)
#   case1: 有环既有入度为2的节点, 去掉环内的边
#   case2: 仅有环, 去掉最后构成环的边
#   case3: 仅有入度为2的节点, 去掉最后形成入度为2节点的边
class Solution:
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        def dfs(source, target):
            if source not in seen:
                seen.add(source)
                if source == target:
                    return True
                return any(dfs(nei, target) for nei in graph[source])
            return False

        graph, graph_degree = collections.defaultdict(set), {}
        isCycle, res_cycle = False, (None, None)
        isDegree2, res_degree1, res_degree2 = False, (None, None), (None, None)

        for u, v in edges:
            seen = set()
            if v in graph and dfs(v, u):
                isCycle, res_cycle = True, (u, v)
            if v in graph_degree.keys():
                isDegree2, res_degree1, res_degree2 = True, (graph_degree[v], v), (u, v)
            else:
                graph_degree[v] = u
            graph[u].add(v)

        if isCycle and isDegree2:
            seen = set()
            return res_degree2 if dfs(res_degree2[1], res_degree2[0]) else res_degree1
        return res_cycle if isCycle else res_degree2


S = Solution()
edges = [[3, 1], [4, 2], [1, 4], [2, 1]]
print(S.findRedundantDirectedConnection(edges))
