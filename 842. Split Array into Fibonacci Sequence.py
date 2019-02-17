# -*- coding: utf-8 -*-
# @Time    : 2019/2/17
# @Author  : qirui
# @FileName: 842. Split Array into Fibonacci Sequence.py

# The same problem: https://leetcode.com/problems/additive-number/
# Backtracking/DFS (general)
class Solution(object):
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """

        def backtrack(tmp, start, preced1=0, preced2=0):
            if start == N:
                if len(tmp) > 2:
                    res.append(tmp)
                    return True
                else:
                    return False

            for i in range(start, N):
                if S[start] == '0' and i > start:
                    break
                sub = int(S[start:i + 1])
                if sub >= pow(2, 31):
                    break
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

        N = len(S)
        res = []
        return res[0] if backtrack([], 0) else []


if __name__ == "__main__":
    S = Solution()
    print(S.splitIntoFibonacci("1101111"))
