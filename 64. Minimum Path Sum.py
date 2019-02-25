# -*- coding: utf-8 -*-
# @Time    : 2019/2/25
# @Author  : qirui
# @FileName: 64. Minimum Path Sum.py

# straightforward DP using DP matrix
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m, n = len(grid), len(grid[0])
        dp = [[float('inf') for _ in range(n + 1)] for _ in range(m + 1)]
        dp[1][1] = grid[0][0]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i + j == 2:  continue
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i - 1][j - 1]
        return dp[m][n]

# straightforward DP not using extra DP matrix
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m, n = len(grid), len(grid[0])
        for i in range(1, n):
            grid[0][i] = grid[0][i - 1] + grid[0][i]
        for j in range(1, m):
            grid[j][0] = grid[j - 1][0] + grid[j][0]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        return grid[m - 1][n - 1]


if __name__ == '__main__':
    S = Solution()
    print(S.minPathSum([
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]))
