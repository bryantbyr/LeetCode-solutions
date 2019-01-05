# -*- coding: utf-8 -*-
# @Time    : 2019/1/5
# @Author  : qirui
# @FileName: 959. Regions Cut By Slashes.py

# Time: O(N^2)
# Space: O(N^2)
# DFS (化归思想, 如何合理化归问题是关键)
class Solution:
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """

        n = 3 * len(grid)
        island = [[0 for _ in range(n)] for _ in range(n)]
        for i, row in enumerate(grid):
            for j, c in enumerate(row):
                if c == "\\":
                    island[i * 3][j * 3] = 1
                    island[i * 3 + 1][j * 3 + 1] = 1
                    island[i * 3 + 2][j * 3 + 2] = 1
                elif c == "/":
                    island[i * 3][j * 3 + 2] = 1
                    island[i * 3 + 1][j * 3 + 1] = 1
                    island[i * 3 + 2][j * 3] = 1

        def dfs(x, y):
            island[x][y] = 1
            for r, c in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= r < n and 0 <= c < n and island[r][c] != 1:
                    dfs(r, c)

        res = 0
        for i in range(n):
            for j in range(n):
                if island[i][j] == 0:
                    res += 1
                    dfs(i, j)
        return res


if __name__ == '__main__':
    S = Solution()
    print(S.regionsBySlashes([
        "\\/",
        "/ "
    ]))
