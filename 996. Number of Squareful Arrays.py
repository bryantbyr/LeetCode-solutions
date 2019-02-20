# -*- coding: utf-8 -*-
# @Time    : 2019/2/19
# @Author  : qirui
# @FileName: 996. Number of Squareful Arrays.py


import math

# Backtracking/DFS (general)
# 该问题本质上全排列问题2, https://leetcode.com/problems/permutations-ii/
class Solution(object):
    def numSquarefulPerms(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        def isValid(tmp, num):
            return len(tmp) == 0 or math.sqrt(tmp[-1] + num) % 1 == 0

        def backtrack(tmp):
            if len(tmp) == N:
                self.ans += 1
                return

            for i in range(N):
                if used[i] or (i > 0 and not used[i - 1] and A[i] == A[i - 1]):   continue
                if isValid(tmp, A[i]):
                    used[i] = True
                    backtrack(tmp + [A[i]])
                    used[i] = False

        N = len(A)
        self.ans = 0
        used = [False for _ in range(N)]
        A.sort()
        backtrack([])
        return self.ans


if __name__ == '__main__':
    S = Solution()
    print(S.numSquarefulPerms([2, 2, 2]))
