# -*- coding: utf-8 -*-
# @Time    : 2018/12/24
# @Author  : qirui
# @FileName: 576. Out of Boundary Paths.py

# Time Limit Exceeded
# class Solution(object):
#     def findPaths(self, m, n, N, i, j):
#         """
#         :type m: int
#         :type n: int
#         :type N: int
#         :type i: int
#         :type j: int
#         :rtype: int
#         """
#
#         self.res = 0
#
#         def dfs(x, y, count):
#             if x < 0 or x > m - 1 or y < 0 or y > n - 1:
#                 self.res += 1
#                 return
#
#             if count < N:
#                 for dir in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#                     dfs(x + dir[0], y + dir[1], count + 1)
#
#         dfs(i, j, 0)
#         return self.res % (10 ** 9 + 7)

import collections

# Learn from discuss
# Time: O(m*n*N)
# Space: O(m*n*N)
# DFS with memorization
class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """

        memo = collections.defaultdict(int)
        mod = 10 ** 9 + 7

        def dfs(x, y, count):
            if (x, y, count) in memo:
                return memo[(x, y, count)]
            if x < 0 or x > m - 1 or y < 0 or y > n - 1:
                return 1
            if count == N:
                return 0
            for dir in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                memo[(x, y, count)] += dfs(x + dir[0], y + dir[1], count + 1)
            return memo[(x, y, count)] % mod

        return dfs(i, j, 0)


if __name__ == '__main__':
    S = Solution()
    print(S.findPaths(m=10, n=10, N=10, i=5, j=5))
