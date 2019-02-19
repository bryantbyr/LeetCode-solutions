# -*- coding: utf-8 -*-
# @Time    : 2019/2/18
# @Author  : qirui
# @FileName: 44. Wildcard Matching.py

# 1706 / 1808 test cases passed.    Status: Time Limit Exceeded
# Backtracking/Recursion/DFS
# class Solution(object):
#     def isMatch(self, s, p):
#         """
#         :type s: str
#         :type p: str
#         :rtype: bool
#         """
#
#         if not p:
#             return not s
#
#         if p[0] == '*':
#             pos = 0
#             while pos < len(p) and p[pos] == '*':
#                 pos += 1
#             return self.isMatch(s, p[pos:]) or (s != "" and self.isMatch(s[1:], p))
#             # return self.isMatch(s, p[1:]) or (s != "" and self.isMatch(s[1:], p))
#         else:
#             first_match = s != "" and (p[0] == s[0] or p[0] == '?')
#             return first_match and self.isMatch(s[1:], p[1:])


# reference:    https://leetcode.com/problems/wildcard-matching/discuss/17812/My-java-DP-solution-using-2D-table
# DP [如何定义最优子问题, 找到递推公式是关键, 填表完成即意味着问题的解决]
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        m, n = len(s), len(p)
        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            if p[i - 1] == '*':
                dp[0][i] = dp[0][i - 1]
            else:
                break

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if (p[j - 1] == s[i - 1] or p[j - 1] == '?') and dp[i - 1][j - 1]:
                    dp[i][j] = True
                elif p[j - 1] == '*' and (dp[i - 1][j] or dp[i][j - 1]):
                    dp[i][j] = True

        return dp[m][n]


if __name__ == '__main__':
    S = Solution()
    print(S.isMatch("aa", "*"))
