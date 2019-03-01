# -*- coding: utf-8 -*-
# @Time    : 2019/2/26
# @Author  : qirui
# @FileName: 97. Interleaving String.py

import collections


# 83 / 101 test cases passed.   Status: Time Limit Exceeded
# Backtracking/DFS/Recursion
# class Solution(object):
#     def isInterleave(self, s1, s2, s3):
#         """
#         :type s1: str
#         :type s2: str
#         :type s3: str
#         :rtype: bool
#         """
#
#         n1, n2, n3 = len(s1), len(s2), len(s3)
#         if n3 != n1 + n2:
#             return False
#
#         dict = collections.defaultdict(list)
#         # for char in set(s1):
#         #     for i in range(n3):
#         #         if char == s3[i]:
#         #             dict[char].append(i)
#         for i in range(n3):
#             if s3[i] in s1:
#                 dict[s3[i]].append(i)
#
#
#         def backtrack(tmp, index, remain):
#             if index == n1:
#                 return remain == s2
#
#             for i in dict[s1[index]]:
#                 if (not tmp or i > tmp[-1]) and backtrack(tmp + [i], index + 1, remain[:(i-index)] + remain[i-index+1:]):
#                     return True
#             return False
#
#         return backtrack([], 0, s3)


# 99 / 101 test cases passed.   Status: Time Limit Exceeded
# Backtracking/DFS/Recursion optimization
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """

        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n3 != n1 + n2:
            return False

        # ******** using `tmp` to mark path ********
        # dict = collections.defaultdict(list)
        # for i in range(n3):
        #     if s3[i] in s1:
        #         dict[s3[i]].append(i)
        #
        # def backtrack(tmp, index, remain):
        #     if index == n1:
        #         return remain == s2
        #     if tmp and remain[:tmp[-1]-index+1] != s2[:tmp[-1]-index+1]:
        #         return False
        #
        #     for i in dict[s1[index]]:
        #         if (not tmp or i > tmp[-1]) and backtrack(tmp + [i], index + 1, remain[:(i - index)] + remain[i - index + 1:]):
        #             return True
        #     return False
        #
        # return backtrack([], 0, s3)

        # ******** no need to use list to mark path  ********
        # def backtrack(pre, index, remain):
        #     if index == n1:
        #         return remain == s2
        #     if pre!=-1 and remain[:pre - index + 1] != s2[:pre - index + 1]:
        #         return False
        #
        #     for i in range(n3):
        #         if s3[i] != s1[index]: continue
        #         if (pre == -1 or i > pre) and backtrack(i, index + 1, remain[:(i - index)] + remain[i - index + 1:]):
        #             return True
        #     return False
        #
        # return backtrack(-1, 0, s3)

        # ****** check completely when backtrack *****
        def backtrack(pre, index, s2_index):
            if index == n1:
                return True
            for i in range(n3):
                if s3[i] != s1[index]: continue
                if (pre == -1 or i > pre) and s3[pre + 1:i] == s2[s2_index:s2_index+i-pre-1] and backtrack(i, index + 1,s2_index+i-pre-1):
                    return True
            return False

        return backtrack(-1, 0,0)

# reference:    https://leetcode.com/problems/interleaving-string/discuss/31888/1ms-tiny-DFS-beats-94.57
# DFS/Backtracking/Recursion with memorization* (a new way to DFS)
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """

        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n3 != n1 + n2:
            return False

        memo = [[True for _ in range(n2 + 1)] for _ in range(n1 + 1)] # key to set memo to be True

        def dfs(index_1, index_2, index_3):
            if index_3 == n3:
                return True
            if not memo[index_1][index_2]:
                return False

            memo[index_1][index_2] = (index_1 < n1 and s1[index_1] == s3[index_3] and dfs(index_1 + 1, index_2, index_3 + 1)) or \
                                     (index_2 < n2 and s2[index_2] == s3[index_3] and dfs(index_1, index_2 + 1, index_3 + 1))

            return memo[index_1][index_2]

        return dfs(0, 0, 0)

# reference:   https://leetcode.com/problems/interleaving-string/discuss/31885/Python-DP-solutions-(O(m*n)-O(n)-space)-BFS-DFS.
# DP converted from above DFS with memorization
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """

        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n3 != n1 + n2:
            return False

        dp = [[True for _ in range(n2 + 1)] for _ in range(n1 + 1)]  # key to set memo to be True
        for j in range(1, n2 + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
        for i in range(1, n1 + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i - 1 + j]) or (dp[i][j - 1] and s2[j - 1] == s3[i - 1 + j])
        return dp[n1][n2]




if __name__ == '__main__':
    S = Solution()
    s1 = "bcbbacbaabaabbbacbbbcbbb"
    s2 = "babcbbacaabbaaaabacc"
    s3 = "bbcbbbcbabacbcbaacabaabaabaabbbaaacccbbabbbb"
    print(S.isInterleave(s1, s2, s3))
