# -*- coding: utf-8 -*-
# @Time    : 2019/2/12
# @Author  : qirui
# @FileName: 78. Subsets.py

# reference: https://leetcode.com/problems/combination-sum/discuss/16502/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)
# Backtrack/DFS (general)
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def backtrack(tmp, start):
            res.append(tmp)
            for i in range(start, N):
                backtrack(tmp + [nums[i]], i + 1)

        N = len(nums)
        res = []
        backtrack([], 0)
        return res


if __name__ == '__main__':
    S = Solution()
    print(S.subsets([1, 2, 3]))
