# -*- coding: utf-8 -*-
# @Time    : 2019/2/12
# @Author  : qirui
# @FileName: 131. Palindrome Partitioning.py

# reference: https://leetcode.com/problems/combination-sum/discuss/16502/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)
# Backtrack/DFS (general)
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        def backtrack(tmp, start):
            if start == N:
                res.append(tmp)
                return
            for i in range(start, N):
                sub = s[start:i + 1]
                if isPalindrome(sub):
                    backtrack(tmp + [sub], i + 1)

        def isPalindrome(s):
            return s == s[::-1]

        N = len(s)
        res = []
        backtrack([], 0)
        return res


if __name__ == '__main__':
    S = Solution()
    print(S.partition("aab"))
