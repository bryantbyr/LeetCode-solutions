# -*- coding: utf-8 -*-
# @Time    : 2019/1/3
# @Author  : qirui
# @FileName: 851. Loud and Rich.py

# Time:O(N^2)
# Space: O(N)
# DFS with memorization
class Solution:
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """

        def dfs(v):
            if memo[v] != -1:
                return memo[v]
            memo[v] = min([quiet[v]] + [dfs(nei) for nei in graph[v]])
            return memo[v]

        N = len(quiet)
        graph = [[] for i in range(N)]
        for x, y in richer:
            graph[y].append(x)

        memo = [-1 for _ in range(N)]
        for i in range(N):
            if memo[i] == -1:
                dfs(i)

        return list(map(lambda x: quiet.index(x), memo))


if __name__ == '__main__':
    S = Solution()
    richer = [[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]]
    quiet = [3, 2, 5, 4, 6, 1, 7, 0]
    print(S.loudAndRich(richer, quiet))
