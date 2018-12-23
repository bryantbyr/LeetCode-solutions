# -*- coding: utf-8 -*-
# @Time    : 2018/12/22
# @Author  : qirui
# @FileName: 416. Partition Equal Subset Sum.py

# Time:O(2^N)
# Space:O(N)
# DFS
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        def dfs(index):
            if index < 0:
                return True

            for i in range(2):
                if nums[index] <= slide_sum[i]:
                    slide_sum[i] -= nums[index]
                    if dfs(index - 1):
                        return True
                    slide_sum[i] += nums[index]
            return False

        if not nums: return False
        target = sum(nums) // 2
        if target * 2 != sum(nums): return False
        slide_sum = [target] * 2
        nums.sort()
        return dfs(len(nums) - 1)

# Time:O(N*M)
# Space:O(N*M)
# DP
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if not nums: return False
        target = sum(nums) // 2
        if target * 2 != sum(nums): return False
        length = len(nums)

        dp = [[False for _ in range(target + 1)] for _ in range(length + 1)]
        for i in range(length + 1):
            dp[i][0] = True

        for i in range(1, length + 1):
            for j in range(1, target + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]

        return dp[length][target]


# Time:O(N*M)
# Space:O(N*M)
# DP (optimize in space)
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if not nums: return False
        target = sum(nums) // 2
        if target * 2 != sum(nums): return False

        dp = [False for _ in range(target + 1)]
        dp[0] = True

        for num in nums:
            for j in range(target,0,-1):
                if j >= num:
                    dp[j] = dp[j] or dp[j - num]

        return dp[target]

if __name__ == '__main__':
    S = Solution()
    print(S.canPartition([1, 5, 11, 5]))
