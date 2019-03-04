# -*- coding: utf-8 -*-
# @Time    : 2019/3/1
# @Author  : qirui
# @FileName: 188. Best Time to Buy and Sell Stock IV.py

# reference:    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
# DP + Greedy
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """

        N = len(prices)
        if N < 2:
            return 0
        if k >= N / 2:
            return sum(i - j for i, j in zip(prices[1:], prices[:-1]) if i - j > 0)

        dp = [[0 for _ in range(N)] for _ in range(k + 1)]
        for K in range(1, k + 1):
            min_to_minus = prices[0]
            for i in range(1, N):
                min_to_minus = min(min_to_minus, prices[i] - dp[K - 1][i - 1])
                dp[K][i] = max(dp[K][i - 1], prices[i] - min_to_minus)
        return dp[k][N - 1]


if __name__ == '__main__':
    S = Solution()
    print(S.maxProfit(2, [2, 4, 1]))
