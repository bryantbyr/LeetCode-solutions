# -*- coding: utf-8 -*-
# @Time    : 2019/2/12
# @Author  : qirui
# @FileName: 90. Subsets II.py

# reference: https://leetcode.com/problems/combination-sum/discuss/16502/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)
# Backtrack/DFS (general)
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def backtrack(tmp, start):
            res.append(tmp)
            for i in range(start, N):
                if i > start and nums[i] == nums[i - 1]:  continue
                backtrack(tmp + [nums[i]], i + 1)

        N = len(nums)
        res = []
        nums.sort()
        backtrack([], 0)
        return res


if __name__ == '__main__':
    S = Solution()
    print(S.subsetsWithDup([1, 2, 2]))
