# -*- coding: utf-8 -*-
# @Time    : 2019/1/3
# @Author  : qirui
# @FileName: 947. Most Stones Removed with Same Row or Column.py

# Time Limit Exceeded:  54 / 68 test cases passed.
# class Solution:
#     def removeStones(self, stones):
#         """
#         :type stones: List[List[int]]
#         :rtype: int
#         """
#
#         def valid(x1, y1, x2, y2):
#             return (x1 - x2) * (y1 - y2) == 0
#
#         def dfs(x, y):
#             if (x, y) in seen:
#                 return 0
#             seen.add((x, y))
#             return 1 + sum(dfs(i, j) for i, j in stones if valid(x, y, i, j))
#
#         seen = set()
#         # return max([dfs(x, y) - 1 for x, y in stones if (x, y) not in seen])
#         return sum([dfs(x, y) - 1 for x, y in stones if (x, y) not in seen])

# 59 / 68 test cases passed. Status: Time Limit Exceeded
# class Solution:
#     def removeStones(self, stones):
#         """
#         :type stones: List[List[int]]
#         :rtype: int
#         """
#
#         def dfs(x, y):
#             seen.add((x, y))
#             return 1 + sum(dfs(i, j) for i, j in stones if (x - i) * (y - j) == 0 and (i, j) not in seen)
#
#         seen = set()
#         return sum([dfs(x, y) - 1 for x, y in stones if (x, y) not in seen])

import collections

# Learn from discuss
# Time: O(N^2)
# Space: O(N^2)
# DFS with adjacent list
class Solution:
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """

        def dfs(x, y):
            seen.add((x, y))
            return 1 + sum(dfs(x, j) for j in row[x] if (x, j) not in seen) \
                   + sum(dfs(i, y) for i in col[y] if (i, y) not in seen)

        row, col = collections.defaultdict(list), collections.defaultdict(list)
        for i, j in stones:
            row[i].append(j)
            col[j].append(i)
        seen = set()
        return sum([dfs(x, y) - 1 for x, y in stones if (x, y) not in seen])


if __name__ == '__main__':
    S = Solution()
    print(S.removeStones([[3, 2], [3, 1], [4, 4], [1, 1], [0, 2], [4, 0]]))
