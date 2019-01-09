# -*- coding: utf-8 -*-
# @Time    : 2019/1/9
# @Author  : qirui
# @FileName: 279. Perfect Squares.py

import math


# 502 / 588 test cases passed.   Time Limit Exceeded
# class Solution(object):
#     def numSquares(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#
#         max_num = int(math.floor(n ** 0.5))
#         queue = [(0, 0)]
#         while queue:
#             num, depth = queue.pop(0)
#             for i in range(1, max_num + 1):
#                 next = num + i ** 2
#                 if next == n:
#                     return depth + 1
#                 queue.append((next, depth + 1))

# Time: O(N^k)
# Space: O(N)
# DFS
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        max_num = int(math.floor(n ** 0.5))
        queue, seen = [(0, 0)], set()
        while queue:
            num, depth = queue.pop(0)
            if num not in seen:
                seen.add(num)
                for i in range(1, max_num + 1):
                    next = num + i ** 2
                    if next == n:
                        return depth + 1
                    elif next > n:
                        break
                    else:
                        queue.append((next, depth + 1))


# Time: O(N^k)
# Space: O(N)
# DFS optimization
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        max_num = int(math.floor(n ** 0.5))
        queue, seen = [(0, 0)], set()
        while queue:
            num, depth = queue.pop(0)
            for i in range(1, max_num + 1):
                next = num + i ** 2
                if next == n:
                    return depth + 1
                elif next > n:
                    break
                elif next not in seen:
                    seen.add(next)
                    queue.append((next, depth + 1))


# Learn from discuss
# Time: O(N^2)
# Space: O(N)
# DP
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [float('inf') for _ in range(n + 1)]
        dp[0] = 0

        for i in range(1, n + 1):
            # j = 0
            # while i - j * j >= 0:
            #     dp[i] = min(dp[i], dp[i - j * j] + 1)
            #     j += 1
            dp[i] = min([dp[i - j * j] + 1 for j in range(1, math.floor(i ** 0.5) + 1)])
        return dp[n]


if __name__ == '__main__':
    S = Solution()
    print(S.numSquares(7168))
