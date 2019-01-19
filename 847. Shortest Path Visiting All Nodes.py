# -*- coding: utf-8 -*-
# @Time    : 2019/1/17
# @Author  : qirui
# @FileName: 847. Shortest Path Visiting All Nodes.py

import copy


# 37 / 46 test cases passed.    Status: Time Limit Exceeded
# class Solution(object):
#     def shortestPathLength(self, graph):
#         """
#         :type graph: List[List[int]]
#         :rtype: int
#         """
#
#         N = len(graph)
#         queue = [(i, set(), set([i])) for i in range(N)]
#         while queue:
#             new_queue = []
#             for node, path, seen in queue:
#                 for nei in graph[node]:
#                     if (node, nei) not in path:
#                         tmp_path = copy.deepcopy(path)
#                         tmp_path.add((node, nei))
#                         tmp_seen = copy.deepcopy(seen)
#                         tmp_seen.add(nei)
#                         if len(tmp_seen) == N:
#                             return len(tmp_path)
#                         new_queue.append((nei, tmp_path, tmp_seen))
#             queue = new_queue
#
#         return 0  # 注意考虑边界条件

# 45 / 46 test cases passed.    Status: Memory Limit Exceeded
# class Solution(object):
#     def shortestPathLength(self, graph):
#         """
#         :type graph: List[List[int]]
#         :rtype: int
#         """
#
#         N = len(graph)
#         queue = [(i, "", str(i)) for i in range(N)]
#         while queue:
#             new_queue = []
#             for node, path, seen in queue:
#                 for nei in graph[node]:
#                     if str((node, nei)) not in path:
#                         tmp_path = path + str((node, nei)) + "."
#                         tmp_seen = seen + "," + str(nei)
#                         if len(set(tmp_seen.split(','))) == N:
#                             return len(tmp_path.split('.')) - 1
#                         new_queue.append((nei, tmp_path, tmp_seen))
#             queue = new_queue
#
#         return 0  # 注意考虑边界条件

# Learn from discuss
# Time: O(N)
# Space: O(N)
# BFS optimization using Bit Manipulation to mark path
class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """

        N = len(graph)
        queue, seen, final_state, step = [(i, 1 << i) for i in range(N)], set(), (1 << N) - 1, 0

        while queue:
            step += 1
            new_queue = []
            for node, state in queue:
                for nei in graph[node]:
                    next_state = state | 1 << nei
                    if next_state == final_state:
                        return step
                    if (nei, next_state) not in seen:
                        seen.add((nei, next_state))
                        new_queue.append((nei, next_state))
            queue = new_queue

        return 0



if __name__ == '__main__':
    S = Solution()
    print(S.shortestPathLength(
        [[1, 4], [0, 3, 4, 7, 9], [6, 10], [1, 10], [1, 0], [6], [7, 2, 5], [6, 1, 8], [7], [1], [2, 3]]))
