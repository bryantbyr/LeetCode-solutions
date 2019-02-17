# -*- coding: utf-8 -*-
# @Time    : 2019/2/17
# @Author  : qirui
# @FileName: 784. Letter Case Permutation.py

# Backtracking/DFS (straightforward)
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """

        def backtrack(tmp, start):
            # if len(tmp) == N:
            #     res.append(tmp)
            #     return
            if start == N:
                res.append(tmp)
                return
            if 'a' <= S[start] <= 'z':
                backtrack(tmp + S[start].upper(), start + 1)
            elif 'A' <= S[start] <= 'Z':
                backtrack(tmp + S[start].lower(), start + 1)
            backtrack(tmp + S[start], start + 1)

            # if len(tmp) == N:
            #     res.append(tmp)
            #     return
            # for i in range(start, N):
            #     if 'a' <= S[i] <= 'z':
            #         backtrack(tmp + S[i].upper(), i + 1)
            #     elif 'A' <= S[i] <= 'Z':
            #         backtrack(tmp + S[i].lower(), i + 1)
            #     backtrack(tmp + S[i], i + 1)

        N = len(S)
        res = []
        backtrack("", 0)
        return res

# Backtracking/DFS (general)
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """

        def backtrack(tmp, start):
            res.append(tmp)
            for i in range(start, N):
                if 'a' <= S[i] <= 'z':
                    backtrack(tmp[:i] + S[i].upper() + tmp[i + 1:], i + 1)
                elif 'A' <= S[i] <= 'Z':
                    backtrack(tmp[:i] + S[i].lower() + tmp[i + 1:], i + 1)

        N = len(S)
        res = []
        backtrack(S, 0)
        return res


if __name__ == '__main__':
    S = Solution()
    print(S.letterCasePermutation("a1b2"))
