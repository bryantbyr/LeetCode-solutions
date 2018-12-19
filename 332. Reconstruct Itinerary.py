# -*- coding: utf-8 -*-
# @Time    : 2018/12/19
# @Author  : qirui
# @FileName: 332. Reconstruct Itinerary.py

import collections
import copy


# Status: Time Limit Exceeded
# class Solution:
#     def findItinerary(self, tickets):
#         """
#         :type tickets: List[List[str]]
#         :rtype: List[str]
#         """
#
#         def make_graph():
#             graph = collections.defaultdict(list)
#             for u,v in tickets:
#                 graph[u].append(v)
#             return graph
#
#         graph = make_graph()
#         res = []
#
#         # def dfs(path,visited_edge,s="",r="JFK"):
#         #     visited_edge = copy.deepcopy(visited_edge)
#         #     if (s,r) in visited_edge:
#         #         return
#         #     visited_edge.add((s,r))
#         #     path+=r
#         #     if len(visited_edge)==len(tickets):
#         #         res.append(path)
#         #         return
#         #     for nei in graph[r]:
#         #         dfs(path,visited_edge,r,nei)
#         #
#         # dfs("",set())
#
#
#         def dfs(path,tickets_left,s="",r="JFK"):
#             tickets_left = copy.deepcopy(tickets_left)
#             # if (s,r) not in tickets_left and s!="":
#             #     return
#             # if (s,r) in tickets_left:
#             #     tickets_left.remove((s,r))
#
#             if [s,r] not in tickets_left and s!="":
#                 return
#             if s!="":
#                 tickets_left.remove([s,r])
#             path+=r
#             if not tickets_left:
#                 res.append(path)
#                 return
#             for nei in graph[r]:
#                 dfs(path,tickets_left,r,nei)
#
#         # tickets_left = list(map(lambda x: tuple(x), tickets))
#         dfs("",tickets)
#
#         ans = min(res)
#         chunks, chunk_size = len(ans), 3
#         return [ans[i:i + chunk_size] for i in range(0, chunks, chunk_size)]

# Learn from discuss
# Time:O(N)
# Space:O(N)
# Hierholzer's algorithm to find a Eulerian path in the graph
class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """

        def make_graph():
            graph = collections.defaultdict(list)
            for u, v in sorted(tickets):
                graph[u].append(v)
            return graph

        graph = make_graph()

        path = []

        def dfs(v="JFK"):
            while graph[v]:
                dfs(graph[v].pop(0))
            path.append(v)

        dfs()
        return path[::-1]


if __name__ == '__main__':
    S = Solution()
    case = [["EZE", "TIA"], ["EZE", "HBA"], ["AXA", "TIA"], ["JFK", "AXA"], ["ANU", "JFK"], ["ADL", "ANU"],
            ["TIA", "AUA"], ["ANU", "AUA"], ["ADL", "EZE"], ["ADL", "EZE"], ["EZE", "ADL"], ["AXA", "EZE"],
            ["AUA", "AXA"], ["JFK", "AXA"], ["AXA", "AUA"], ["AUA", "ADL"], ["ANU", "EZE"], ["TIA", "ADL"],
            ["EZE", "ANU"], ["AUA", "ANU"]]
    print(S.findItinerary(case))
