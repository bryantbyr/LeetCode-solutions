# -*- coding: utf-8 -*-
# @Time    : 2019/3/5
# @Author  : qirui
# @FileName: 300. Longest Increasing Subsequence.py

# # DP
# class Solution(object):
#     def lengthOfLIS(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#
#         if not nums:    return 0
#
#         N = len(nums)
#         dp = [1 for _ in range(N)]
#         ans = 1
#         for i in range(1, N):
#             tmp = 1
#             for j in range(i):
#                 if nums[i] > nums[j]:
#                     tmp = max(tmp, dp[j] + 1)
#             dp[i] = tmp
#             ans = max(ans, dp[i])
#         return ans


# Time: O(N^2)
# Space: O(N)
# DP (similar to https://leetcode.com/problems/palindrome-partitioning-ii/)
# 1. dp[i]: 以nums[i]为末尾元素的最大递增子序列的长度
# 2. dp[i] = max(dp[i],dp[j-1]+1) j=0...i-1
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:    return 0

        N = len(nums)
        dp = [1 for _ in range(N)]
        ans = 1
        for i in range(1, N):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            ans = max(ans, dp[i])
        return ans


if __name__ == '__main__':
    S = Solution()
    print(S.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
