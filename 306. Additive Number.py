# -*- coding: utf-8 -*-
# @Time    : 2019/2/15
# @Author  : qirui
# @FileName: 306. Additive Number.py

# Backtracking/DFS (general)
class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """

        def backtrack(tmp, start, preced1=0, preced2=0):
            if start == N:
                return len(tmp) > 2
            for i in range(start, N):
                if num[start] == '0' and i > start:
                    break
                sub = int(num[start:i + 1])
                if not tmp:
                    preced1 = sub
                    if backtrack(tmp + [sub], i + 1, preced1, preced2):
                        return True
                elif len(tmp) == 1:
                    preced2 = sub
                    if backtrack(tmp + [sub], i + 1, preced1, preced2):
                        return True
                else:
                    if preced1 + preced2 == sub:
                        if backtrack(tmp + [sub], i + 1, preced2, sub):
                            return True
            return False

        N = len(num)
        return backtrack([], 0)


if __name__ == '__main__':
    S = Solution()
    print(S.isAdditiveNumber("1203"))
