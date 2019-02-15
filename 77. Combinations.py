# -*- coding: utf-8 -*-
# @Time    : 2019/2/15
# @Author  : qirui
# @FileName: 77. Combinations.py


# Backtrack/DFS (general)
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        def backtrack(tmp, start):
            if len(tmp) == k:
                res.append(tmp)
                return
            for i in range(start, n + 1):
                backtrack(tmp + [i], i + 1)

        res = []
        backtrack([], 1)
        return res


if __name__ == '__main__':
    S = Solution()
    print(S.combine(4, 2))
