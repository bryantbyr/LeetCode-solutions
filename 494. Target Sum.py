# -*- coding: utf-8 -*-
# @Time    : 2018/12/23
# @Author  : qirui
# @FileName: 494. Target Sum.py

# Time Limit Exceeded
# Time:O(2^N)
# Space:O(N)
# DFS
# class Solution(object):
#     def findTargetSumWays(self, nums, S):
#         """
#         :type nums: List[int]
#         :type S: int
#         :rtype: int
#         """
#
#         def dfs(index, target):
#             if index < 0:
#                 if target == S:
#                     self.ans += 1
#                 return
#             dfs(index - 1, target + nums[index])
#             dfs(index - 1, target - nums[index])
#
#         self.ans = 0
#         dfs(len(nums) - 1, 0)
#         return self.ans


# Learn from discuss
# Time:O(N^2)
# Space:O(N)
# DP
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """

        _sum = sum(nums)
        # if (_sum + S) & 1 == 1: return 0
        if _sum < S or (_sum + S) & 1 == 1: return 0

        target = (_sum + S) // 2
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1

        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] += dp[i - num]

        return dp[target]


if __name__ == '__main__':
    S = Solution()
    print(S.findTargetSumWays([0, 0, 0, 0, 0, 0, 0, 0, 1]
                              , 1))
