# -*- coding: utf-8 -*-
# @Time    : 2019/3/5
# @Author  : qirui
# @FileName: 174. Dungeon Game.py

# reference:    https://leetcode.com/problems/dungeon-game/discuss/52774/C%2B%2B-DP-solution
# DP
# 解题的关键是发现正确的最优子问题！
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """

        # m, n = len(dungeon), len(dungeon[0])
        # dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        # cur = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        #
        # for i in range(1, m + 1):
        #     if dungeon[i - 1][0] + cur[i - 1][1] < 1:
        #         dp[i][1] = (1 - dungeon[i - 1][0] - cur[i - 1][1]) + dp[i - 1][1]
        #         cur[i][1] = 1
        #     else:
        #         dp[i][1] = dp[i - 1][1]
        #         cur[i][1] = cur[i - 1][1] + dungeon[i - 1][0]
        #
        # for j in range(1, n + 1):
        #     if dungeon[0][j - 1] + cur[1][j - 1] < 1:
        #         dp[1][j] = (1 - dungeon[0][j - 1] - cur[1][j - 1]) + dp[1][j - 1]
        #         cur[1][j] = 1
        #     else:
        #         dp[1][j] = dp[1][j - 1]
        #         cur[1][j] = cur[1][j - 1] + dungeon[0][j - 1]
        #
        #
        # for i in range(2, m + 1):
        #     for j in range(2, n + 1):
        #         if dungeon[i - 1][j - 1] + cur[i - 1][j] < 1:
        #             if dungeon[i - 1][j - 1] + cur[i][j - 1] < 1:
        #                 dp[i][j] = min((1 - dungeon[i - 1][j - 1] - cur[i - 1][j]) + dp[i - 1][j],
        #                                (1 - dungeon[i - 1][j - 1] - cur[i][j - 1]) + dp[i][j - 1])
        #                 cur[i][j] = 1
        #             else:
        #                 if (1 - dungeon[i - 1][j - 1] - cur[i - 1][j]) + dp[i - 1][j] > dp[i][j - 1]:
        #                     dp[i][j] = dp[i][j - 1]
        #                     cur[i][j] = cur[i][j - 1] + dungeon[i - 1][j - 1]
        #                 else:
        #                     dp[i][j] = (1 - dungeon[i - 1][j - 1] - cur[i - 1][j]) + dp[i - 1][j]
        #                     cur[i][j] = 1
        #         else:
        #             if dungeon[i - 1][j - 1] + cur[i][j - 1] < 1:
        #                 if dp[i - 1][j] > (1 - dungeon[i - 1][j - 1] - cur[i][j - 1]) + dp[i][j - 1]:
        #                     dp[i][j] = (1 - dungeon[i - 1][j - 1] - cur[i][j - 1]) + dp[i][j - 1]
        #                     cur[i][j] = 1
        #                 else:
        #                     dp[i][j] = dp[i - 1][j]
        #                     cur[i][j] = cur[i - 1][j] + dungeon[i - 1][j - 1]
        #             else:
        #                 if dp[i - 1][j] > dp[i][j - 1]:
        #                     dp[i][j] = dp[i][j - 1]
        #                     cur[i][j] = cur[i][j - 1] + dungeon[i - 1][j - 1]
        #                 else:
        #                     dp[i][j] = dp[i - 1][j]
        #                     cur[i][j] = cur[i - 1][j] + dungeon[i - 1][j - 1]
        #
        # return dp[m][n] if dp[m][n] != 0 else 1

        m, n = len(dungeon), len(dungeon[0])
        dp = [[float('inf') for _ in range(n + 1)] for _ in range(m + 1)]
        dp[m][n - 1] = dp[m - 1][n] = 1
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                tmp = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]
                dp[i][j] = tmp if tmp > 0 else 1

        return dp[0][0]


if __name__ == '__main__':
    S = Solution()
    print(S.calculateMinimumHP([[1, -3, 3],
                                [0, -2, 0],
                                [-3, -3, -3]]))
