# -*- coding: utf-8 -*-
# @Time    : 2019/3/1
# @Author  : qirui
# @FileName: 123. Best Time to Buy and Sell Stock III.py

# 199 / 200 test cases passed.  Status: Time Limit Exceeded
# reference: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/135704/Detail-explanation-of-DP-solution
# DP
# dp[k, i] = max(dp[k, i-1], prices[i] - prices[j] + dp[k-1, j-1]), j=[0..i-1]
# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#
#         if not prices:
#             return 0
#
#         N = len(prices)
#         dp = [[0 for _ in range(N)] for _ in range(3)]
#         for k in range(1, 3):
#             for i in range(1, N):
#                 min_to_minus = prices[0]
#                 for j in range(1, i):
#                     min_to_minus = min(min_to_minus, prices[j] - dp[k - 1][j - 1])
#                 dp[k][i] = max(dp[k][i - 1], prices[i] - min_to_minus)
#         return dp[2][N - 1]


# above DP optimization
# Time: O(K*N)
# Space: O(K*N)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if not prices:
            return 0

        N = len(prices)
        dp = [[0 for _ in range(N)] for _ in range(3)]
        for k in range(1, 3):
            min_to_minus = prices[0]
            for i in range(1, N):
                min_to_minus = min(min_to_minus, prices[i] - dp[k - 1][i - 1])
                dp[k][i] = max(dp[k][i - 1], prices[i] - min_to_minus)
        return dp[2][N - 1]


if __name__ == '__main__':
    S = Solution()
    print(S.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
