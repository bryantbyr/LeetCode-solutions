# -*- coding: utf-8 -*-
# @Time    : 2019/1/28
# @Author  : qirui
# @FileName: 17. Letter Combinations of a Phone Number.py

# Time: O(N^3)
# Space: O(N)
# DFS / Backtracking
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if not digits:
            return []

        dict = {"2": ['a', 'b', 'c'], "3": ['d', 'e', 'f'], "4": ['g', 'h', 'i'], "5": ['j', 'k', 'l'],
                "6": ['m', 'n', 'o'], "7": ['p', 'q', 'r', 's'], "8": ['t', 'u', 'v'], "9": ['w', 'x', 'y', 'z']}

        def dfs(index, tmp):
            if index == N:
                res.append(tmp)
                return
            for alp in dict[digits[index]]:
                dfs(index + 1, tmp + alp)

        N = len(digits)
        res = []
        dfs(0, "")
        return res

# Time: O(N^3)
# Space: O(N)
# iteration
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if not digits:
            return []

        dict = {"2": ['a', 'b', 'c'], "3": ['d', 'e', 'f'], "4": ['g', 'h', 'i'], "5": ['j', 'k', 'l'],
                "6": ['m', 'n', 'o'], "7": ['p', 'q', 'r', 's'], "8": ['t', 'u', 'v'], "9": ['w', 'x', 'y', 'z']}

        res = [""]
        for digit in digits:
            tmp = []
            # for alph in dict[digit]:
            #     for item in res:
            #         tmp.append(item + alph)
            for item in res:
                for alph in dict[digit]:
                    tmp.append(item + alph)
            res = tmp
        return res


# Learn from discuss
# Recursion
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if not digits:
            return []

        dict = {"2": ['a', 'b', 'c'], "3": ['d', 'e', 'f'], "4": ['g', 'h', 'i'], "5": ['j', 'k', 'l'],
                "6": ['m', 'n', 'o'], "7": ['p', 'q', 'r', 's'], "8": ['t', 'u', 'v'], "9": ['w', 'x', 'y', 'z']}

        if len(digits) == 1:
            return dict[digits[0]]

        prev = self.letterCombinations(digits[:-1])
        cur = digits[-1]
        return [s + v for s in prev for v in dict[cur]]


if __name__ == '__main__':
    S = Solution()
    print(S.letterCombinations("23"))
