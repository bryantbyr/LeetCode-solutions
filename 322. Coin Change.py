# -*- coding: utf-8 -*-
# @Time    : 2019/3/6
# @Author  : qirui
# @FileName: 322. Coin Change.py

# 15 / 182 test cases passed.     Status: Time Limit Exceeded
# Backtracking/DFS/Recursion (general)
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        def backtrack(sum, cnt):
            if cnt >= self.ans:
                return
            if sum == amount:
                self.ans = min(self.ans, cnt)
                return
            if sum > amount:
                return
            for coin in coins:
                backtrack(sum + coin, cnt + 1)

        self.ans = float('inf')
        coins.sort(reverse=True)
        backtrack(0, 0)
        return self.ans if self.ans != float('inf') else -1


import collections


# Backtracking/DFS/Recursion with memorization
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        def backtrack(remain):
            if remain in memo:
                return memo[remain]
            if remain < 0:
                return float('inf')
            if remain == 0:
                return 0

            memo[remain] = min([backtrack(remain - coin) for coin in coins]) + 1
            return memo[remain]

        memo = collections.defaultdict(int)
        # coins.sort(reverse=True)
        res = backtrack(amount)
        return res if res != float('inf') else -1


# standard DP converted from above solution
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        dp = [float('inf') for _ in range(amount + 1)]
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1


if __name__ == '__main__':
    S = Solution()
    print(S.coinChange([1, 2, 5], 100))
