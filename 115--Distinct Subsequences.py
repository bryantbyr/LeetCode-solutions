# /usr/bin/env python3
# -*- conding:utf-8 -*-


class Solution(object):
    """docstring for Solution"""

    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m = len(s)
        n = len(t)
        dp = [[[]for j in range(n + 1)]for i in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = 1
        for i in range(m + 1):
            for j in range(i + 1, n + 1):
                dp[i][j] = 0
        for i in range(1, m + 1):
            for j in range(1, min(n + 1, i + 1)):
                if s[m - i] == t[n - j]:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[m][n]


S = Solution()
print(S.numDistinct('rabbit', 'rabit'))
