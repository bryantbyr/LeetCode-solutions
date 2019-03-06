# -*- coding: utf-8 -*-
# @Time    : 2019/3/6
# @Author  : qirui
# @FileName: 309. Best Time to Buy and Sell Stock with Cooldown.py

# # Time: O(N^2)
# # Space: O(N)
# # DP
# # 1. dp[i]: max profit ended at day i
# # 2. dp[i] = max(dp[i - 1], dp[i], prices[i] - prices[j] + dp[j - 2]) j=0...(i-1)
# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#
#         if not prices:  return 0
#
#         N = len(prices)
#         dp = [0 for _ in range(N)]
#         for i in range(1, N):
#             tmp = 0
#             for j in range(i):
#                 if prices[i] > prices[j]:
#                     tmp = max(tmp, prices[i] - prices[j] + dp[j - 2] if j >= 2 else prices[i] - prices[j])
#             dp[i] = max(tmp, dp[i - 1])
#
#             # for j in range(i):
#             #     if prices[i] > prices[j]:
#             #         dp[i] = max(dp[i], dp[i - 1], prices[i] - prices[j] + dp[j - 2] if j >= 2 else prices[i] - prices[j])
#             # if dp[i] == 0:
#             #     dp[i] = dp[i - 1]
#
#         return dp[N - 1]

# reference:    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75931/Easiest-JAVA-solution-with-explanations
# Time: O(N)
# Space: O(N)
# Better DP
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if not prices:  return 0

        b0 = -prices[0]
        b1 = b0
        s0, s1, s2 = 0, 0, 0

        for i in range(1, len(prices)):
            b0 = max(b1, s2 - prices[i])
            s0 = max(s1, b1 + prices[i])
            b1 = b0
            s1, s2 = s0, s1
        return s0


if __name__ == '__main__':
    S = Solution()
    print(S.maxProfit([4, 1, 2, 1, 0]))
