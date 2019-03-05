# -*- coding: utf-8 -*-
# @Time    : 2019/3/1
# @Author  : qirui
# @FileName: 132. Palindrome Partitioning II.py

# reference:    https://leetcode.com/problems/palindrome-partitioning-ii/discuss/42213/Easiest-Java-DP-Solution-(97.36)
# DP
# key: 两重DP非常巧妙, 判断回文字符串也可用DP优化
# Time: O(N^2)
# Space: O(N^2)
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """

        N = len(s)
        pali = [[False for _ in range(N)] for _ in range(N)]
        dp = [0 for _ in range(N)]
        for i in range(N):
            tmp_min = i
            for j in range(i + 1):
                if s[j] == s[i] and (j + 1 > i - 1 or pali[j + 1][i - 1]):
                    pali[j][i] = True
                    tmp_min = 0 if j == 0 else min(tmp_min, dp[j - 1] + 1)
            dp[i] = tmp_min
        return dp[N - 1]


if __name__ == '__main__':
    S = Solution()
    print(S.minCut("aab"))
