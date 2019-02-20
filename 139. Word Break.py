# -*- coding: utf-8 -*-
# @Time    : 2019/2/19
# @Author  : qirui
# @FileName: 139. Word Break.py

# DP
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        N = len(s)
        dp = [False for _ in range(N + 1)]
        dp[0] = True

        for i in range(1, N + 1):
            for j in range(i):
                # sub = s[j:i]
                # if sub in wordDict:
                #     dp[i] = dp[j]
                #     if dp[i]:
                #         break
                if s[j:i] in wordDict and dp[j]:
                    dp[i] = True
                    break
        return dp[N]


if __name__ == '__main__':
    S = Solution()
    s = "leetcode"
    wordDict = ["leet", "code"]
    print(S.wordBreak(s, wordDict))
