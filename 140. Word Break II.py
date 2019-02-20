# -*- coding: utf-8 -*-
# @Time    : 2019/2/19
# @Author  : qirui
# @FileName: 140. Word Break II.py

# 31 / 39 test cases passed.    Status: Time Limit Exceeded
# Backtracking/DFS (general)
# class Solution(object):
#     def wordBreak(self, s, wordDict):
#         """
#         :type s: str
#         :type wordDict: List[str]
#         :rtype: List[str]
#         """
#
#         def backtrack(tmp, start):
#             if start == N:
#                 res.append(" ".join(tmp))
#                 return
#
#             for i in range(start, N):
#                 sub = s[start:i + 1]
#                 if sub in wordDict:
#                     backtrack(tmp + [sub], i + 1)
#
#         N = len(s)
#         res = []
#         backtrack([], 0)
#         return res

# reference:    https://leetcode.com/problems/word-break-ii/discuss/44185/Getting-rid-of-TLE
# Backtracking/DFS (general) + DP
# Firstly, to check whether s is breakable to avoid TLE using DP. Then use Backtracking/DFS to find the answer.
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        def backtrack(tmp, start):
            if start == N:
                res.append(" ".join(tmp))
                return

            for i in range(start, N):
                sub = s[start:i + 1]
                if sub in wordDict:
                    backtrack(tmp + [sub], i + 1)

        N = len(s)
        dp = [False for _ in range(N + 1)]
        dp[0] = True
        for i in range(1, N + 1):
            for j in range(i):
                if s[j:i] in wordDict and dp[j]:
                    dp[i] = True
                    break

        res = []
        if dp[N]:
            backtrack([], 0)
        return res


if __name__ == '__main__':
    S = Solution()
    # s = "pineapplepenapple"
    # wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
    print(S.wordBreak(s, wordDict))
