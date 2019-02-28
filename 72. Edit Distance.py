# -*- coding: utf-8 -*-
# @Time    : 2019/2/26
# @Author  : qirui
# @FileName: 72. Edit Distance.py

# https://leetcode.com/problems/edit-distance/discuss/25849/Java-DP-solution-O(nm)
# DP
# 1. dp[i][j]: minimum distance for "first i characters of word1 to match first j characters of word2"
# 2. dp[i][j] = dp[i - 1][j - 1]    if word1[i-1] == word2[j-1]
#    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1   if word1[i-1] != word2[j-1]
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j - 1] if word1[i - 1] == word2[j - 1] else min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        return dp[m][n]


if __name__ == '__main__':
    S = Solution()
    word1 = "horse"
    word2 = "ros"
    print(S.minDistance(word1, word2))
