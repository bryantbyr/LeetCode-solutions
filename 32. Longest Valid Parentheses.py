# -*- coding: utf-8 -*-
# @Time    : 2019/2/23
# @Author  : qirui
# @FileName: 32. Longest Valid Parentheses.py

# reference:    https://leetcode.com/problems/longest-valid-parentheses/solution/
# DP
# DP两大关键点:  1. 如何定义最优子问题,即dp[i]  2. 尝试寻找最优子问题dp[i]之间的递归关系(公式)
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        N = len(s)
        dp = [0 for i in range(N + 1)]
        ans = 0
        for i in range(2, N + 1):
            # if s[i - 1] == ')' and s[i - 2] == '(':
            #     dp[i] = dp[i - 2] + 2
            # elif s[i - 1] == ')' and s[i - 2] == ')' and i - dp[i - 1] - 2 >= 0 and s[i - dp[i - 1] - 2] == '(':
            #     dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
            # ans = max(ans, dp[i])
            if s[i - 1] == ')':
                if s[i - 2] == '(':
                    dp[i] = dp[i - 2] + 2
                elif s[i - 2] == ')' and i - dp[i - 1] - 2 >= 0 and s[i - dp[i - 1] - 2] == '(':
                    dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
                ans = max(ans, dp[i])
        return ans


if __name__ == '__main__':
    S = Solution()
    print(S.longestValidParentheses("(()))())("))
