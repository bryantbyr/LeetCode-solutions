# 834. Sum of Distances in Tree

import collections


# Time Limit Exceeded O(N^2)
# class Solution:
#     def sumOfDistancesInTree(self, N, edges):
#         """
#         :type N: int
#         :type edges: List[List[int]]
#         :rtype: List[int]
#         """
#
#         conn = collections.defaultdict(set)
#         for edge in edges:
#             conn[edge[0]].add(edge[1])
#             conn[edge[1]].add(edge[0])
#
#         res = [0] * N
#
#         def dfs(i, con, depth):
#             for x in conn[con]:
#                 if x not in seen:
#                     seen.add(x)
#                     res[i] += depth
#                     dfs(i, x, depth + 1)
#
#         for i in range(N):
#             seen = {i}
#             dfs(i, i, 1)
#
#         return res

#Learn from Solution on 20181202
#Time:O(N)
#Space:O(N)
#Tree + DFS + DP
class Solution:
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        conn = collections.defaultdict(set)
        for edge in edges:
            conn[edge[0]].add(edge[1])
            conn[edge[1]].add(edge[0])

        res = [0] * N
        count = [0] * N

        def dfs1(root=0, seen=set()):
            seen.add(root)
            for x in conn[root]:
                if x not in seen:
                    dfs1(x, seen)
                    count[root] += count[x]
                    res[root] += res[x] + count[x]
            count[root] += 1

        def dfs2(root=0, seen=set()):
            seen.add(root)
            for x in conn[root]:
                if x not in seen:
                    res[x] = res[root] - count[x] + (N - count[x])
                    dfs2(x, seen)

        dfs1()
        dfs2()

        return res


S = Solution()
print(S.sumOfDistancesInTree(6, [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]))
