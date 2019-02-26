# -*- coding: utf-8 -*-
# @Time    : 2019/2/25
# @Author  : qirui
# @FileName: 213. House Robber II.py

# DP
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        N = len(nums)
        if N == 0: return 0
        if N == 1: return nums[0]
        if N == 2: return max(nums[0], nums[1])

        dp = [0 for _ in range(N + 1)]
        dp[1], dp[2] = nums[0], max(nums[0], nums[1])
        for i in range(3, N - 1):
            dp[i] = max(nums[i - 1] + dp[i - 2], nums[i - 2] + dp[i - 3])
        ans = max(dp[N - 3] + nums[N - 2], dp[N - 2])

        dp[1], dp[2] = nums[1], max(nums[1], nums[2])
        for i in range(3, N):
            dp[i] = max(nums[i] + dp[i - 2], nums[i - 1] + dp[i - 3])
        return max(ans, dp[N - 1])


# DP optimization with O(1) space
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        N = len(nums)
        if N == 0: return 0
        if N < 4: return max(nums)

        a, b, c = 0, nums[0], max(nums[0], nums[1])
        for i in range(3, N - 1):
            d = c
            c, a, b = max(nums[i - 1] + b, nums[i - 2] + a), b, d
        ans = max(b + nums[N - 2], c)

        a, b, c = 0, nums[1], max(nums[1], nums[2])
        for i in range(3, N):
            d = c
            c, a, b = max(nums[i] + b, nums[i - 1] + a), b, d
        return max(ans, c)


if __name__ == '__main__':
    S = Solution()
    print(S.rob([2, 3, 2]))
