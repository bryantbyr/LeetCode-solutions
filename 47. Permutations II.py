# -*- coding: utf-8 -*-
# @Time    : 2019/2/12
# @Author  : qirui
# @FileName: 47. Permutations II.py

# reference: https://leetcode.com/problems/combination-sum/discuss/16502/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)
# Backtrack/DFS (general)
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def backtrack(tmp):
            if len(tmp) == N:
                res.append(tmp)
                return
            for i in range(N):
                if used[i] or (i > 0 and not used[i - 1] and nums[i] == nums[i - 1]):   continue
                used[i] = True
                backtrack(tmp + [nums[i]])
                used[i] = False

        N = len(nums)
        res = []
        used = [False for _ in range(N)]
        nums.sort()
        backtrack([])
        return res


if __name__ == '__main__':
    S = Solution()
    print(S.permuteUnique([1, 1, 2]))
