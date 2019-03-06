# -*- coding: utf-8 -*-
# @Time    : 2019/3/5
# @Author  : qirui
# @FileName: 221. Maximal Square.py

# # reference:    https://leetcode.com/problems/maximal-square/solution/
# # DP
# # 本题的DP思路较为巧妙,以DP思想求最大边,转而求最大面积,递归关系的发现需要对问题本质有深刻的认识
# class Solution(object):
#     def maximalSquare(self, matrix):
#         """
#         :type matrix: List[List[str]]
#         :rtype: int
#         """
#
#         if not matrix:  return 0
#
#         m, n = len(matrix), len(matrix[0])
#         dp = [[0 for _ in range(n)] for _ in range(m)]
#         max_len = 0
#         for i in range(m):
#             if matrix[i][0] == '1':
#                 dp[i][0] = 1
#                 max_len = 1
#         for j in range(1, n):
#             if matrix[0][j] == '1':
#                 dp[0][j] = 1
#                 max_len = 1
#
#         for i in range(1, m):
#             for j in range(1, n):
#                 if matrix[i][j] == '1':
#                     dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
#                     max_len = max(max_len, dp[i][j])
#         return max_len * max_len

# reference:    https://leetcode.com/problems/maximal-square/solution/
# DP
# 本题的DP思路较为巧妙,以DP思想求最大边,转而求最大面积,递归关系的发现需要对问题本质有深刻的认识
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        if not matrix:  return 0

        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        max_len = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    max_len = max(max_len, dp[i][j])
        return max_len * max_len


if __name__ == '__main__':
    S = Solution()
    print(S.maximalSquare([["1", "0", "1", "0", "0"],
                           ["1", "0", "1", "1", "1"],
                           ["1", "1", "1", "1", "1"],
                           ["1", "0", "0", "1", "0"]]))
