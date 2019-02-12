# -*- coding: utf-8 -*-
# @Time    : 2019/1/28
# @Author  : qirui
# @FileName: 39. Combination Sum.py

# DFS/Backtracking
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def dfs(tmp, sum):
            if sum == target:
                new_permutation = sorted(tmp)
                if new_permutation not in res:
                    res.append(new_permutation)
                return
            for num in candidates:
                if sum + num <= target:
                    dfs(tmp[:] + [num], sum + num)

        res = []
        dfs([], 0)
        return res

# Backtracking/DFS
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def dfs(tmp, sum):
            if sum == target:
                new_permutation = sorted(tmp)
                if new_permutation not in res:
                    res.append(new_permutation)
                return
            for num in candidates:
                if sum + num <= target:
                    tmp.append(num)
                    dfs(tmp, sum + num)
                    tmp.remove(num)

        res = []
        dfs([], 0)
        return res

# DFS/Backtracking optimization
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def dfs(index, tmp, sum):
            if sum == target:
                res.append(tmp[:])
                return
            for i in range(index, len(candidates)):
                if sum + candidates[i] <= target:
                    tmp.append(candidates[i])
                    dfs(i, tmp, sum + candidates[i])
                    tmp.remove(candidates[i])

        candidates.sort(reverse=True)
        res = []
        dfs(0, [], 0)
        return res


# DFS/Backtracking (A new way for recursion)
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def dfs(cur_index, tmp, sum):
            if sum == target:
                res.append(tmp[:])
                return
            elif sum > target:
                return
            for i in range(cur_index, N):
                tmp.append(candidates[i])
                dfs(i, tmp, sum + candidates[i])
                tmp.remove(candidates[i])

        candidates.sort(reverse=True)
        N = len(candidates)
        res = []
        dfs(0, [], 0)
        return res


if __name__ == '__main__':
    S = Solution()
    print(S.combinationSum([2, 3, 6, 7], 7))
