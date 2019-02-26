# -*- coding: utf-8 -*-
# @Time    : 2019/2/25
# @Author  : qirui
# @FileName: 198. House Robber.py

# DP
# 1.dp[i]: 前i个元素的最优解    2.dp[i] = max(dp[i-2]+nums[i-1],dp[i-3]+nums[i-2])
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        N = len(nums)
        if N == 0: return 0
        if N == 1: return nums[0]
        # if N == 2: return max(nums[0], nums[1])
        dp = [0 for _ in range(N + 1)]
        dp[1], dp[2] = nums[0], max(nums[0], nums[1])
        for i in range(3, N + 1):
            dp[i] = max(nums[i - 1] + dp[i - 2], nums[i - 2] + dp[i - 3])
        return dp[N]

# DP optimization with O(1) space
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        N = len(nums)
        if N == 0: return 0
        if N == 1: return nums[0]
        a, b, c = 0, nums[0], max(nums[0], nums[1])
        for i in range(3, N + 1):
            d = c
            c = max(nums[i - 1] + b, nums[i - 2] + a)
            a, b = b, d
        return c


if __name__ == '__main__':
    S = Solution()
    print(S.rob([1, 2, 3, 1]))
