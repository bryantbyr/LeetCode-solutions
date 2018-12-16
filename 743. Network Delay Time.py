# 743. Network Delay Time

import collections

# Learn from discuss on 20181216
# Time:O(N^2)
# Space:(N)
# Dijkstra's Algorithm *
class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """

        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dist = {node: float('inf') for node in range(1, N + 1)}
        dist[K] = 0
        seen = [False] * (N + 1)

        while True:
            cand_node = -1
            cand_dist = float('inf')
            for i in range(1, N + 1):
                if not seen[i] and dist[i] < cand_dist:
                    cand_dist = dist[i]
                    cand_node = i

            if cand_node == -1: break
            seen[cand_node] = True
            for nei, d in graph[cand_node]:
                if not seen[nei]:
                    dist[nei] = min(dist[nei], dist[cand_node] + d)

        ans = max(dist.values())
        return ans if ans < float('inf') else -1


if __name__ == '__main__':
    S = Solution()
    print(S.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
