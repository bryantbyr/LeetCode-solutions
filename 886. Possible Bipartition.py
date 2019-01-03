# -*- coding: utf-8 -*-
# @Time    : 2019/1/3
# @Author  : qirui
# @FileName: 886. Possible Bipartition.py

class Solution:
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
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

        graph = [[] for _ in range(N + 1)]
        for edge in dislikes:
            if edge:
                graph[edge[0]].append(edge[1])
                graph[edge[1]].append(edge[0])

        colors = [0 for _ in range(N + 1)]
        for i in range(1, N + 1):
            if colors[i] == 0 and not dfs(i, 1):
                return False
        return True


if __name__ == '__main__':
    S = Solution()
    print(S.possibleBipartition(4, [[1, 2], [1, 3], [2, 4]]))
