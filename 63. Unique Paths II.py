# -*- coding: utf-8 -*-
# @Time    : 2019/2/23
# @Author  : qirui
# @FileName: 63. Unique Paths II.py

# easy and standard DP
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i + j > 0 and obstacleGrid[i][j] == 0:
                    dp[i][j] = (dp[i - 1][j] if i > 0 and obstacleGrid[i - 1][j] == 0 else 0) + \
                               (dp[i][j - 1] if j > 0 and obstacleGrid[i][j - 1] == 0 else 0)
        return dp[m - 1][n - 1]


# DP not using extra matrix
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        obstacleGrid[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        for i in range(m):
            for j in range(n):
                if i + j == 0:  continue
                obstacleGrid[i][j] = (obstacleGrid[i - 1][j] if i > 0 else 0) + (obstacleGrid[i][j - 1] if j > 0 else 0) if obstacleGrid[i][j] == 0 else 0
        return obstacleGrid[m - 1][n - 1]


if __name__ == '__main__':
    S = Solution()
    print(S.uniquePathsWithObstacles([
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]))
