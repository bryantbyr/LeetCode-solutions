# -*- coding: utf-8 -*-
# @Time    : 2019/2/23
# @Author  : qirui
# @FileName: 120. Triangle.py

# DP with O(N^2) space
# 1. dp[i][j]: minimum sum from (i,j) to bottom     2. dp[i][j] = min(dp[i+1][j],dp[i+1][j+1]) + triangle[i][j]
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        N = len(triangle)
        dp = [[0 for _ in range(N)] for _ in range(N)]
        dp[-1] = triangle[-1]
        for layer in range(N - 2, -1, -1):
            for index in range(layer + 1):
                dp[layer][index] = min(dp[layer + 1][index], dp[layer + 1][index + 1]) + triangle[layer][index]
        return dp[0][0]

# reference:    https://leetcode.com/problems/triangle/discuss/38730/DP-Solution-for-Triangle
# DP optimization with O(N) space
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        N = len(triangle)
        dp = triangle[-1]
        for layer in range(N - 2, -1, -1):
            for index in range(layer + 1):
                dp[index] = min(dp[index], dp[index + 1]) + triangle[layer][index]
        return dp[0]


if __name__ == '__main__':
    S = Solution()
    print(S.minimumTotal([
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]))
