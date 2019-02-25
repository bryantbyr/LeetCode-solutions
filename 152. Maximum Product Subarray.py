# -*- coding: utf-8 -*-
# @Time    : 2019/2/25
# @Author  : qirui
# @FileName: 152. Maximum Product Subarray.py

# reference:    https://leetcode.com/problems/maximum-product-subarray/discuss/48261/Share-my-DP-code-that-got-AC
# DP
# 1. max_product[i]: maximum product ended at index i, min_product[i]: min_product product ended at index i
# 2. max_product[i] = max(min_product[i - 1] * nums[i], max_product[i - 1] * nums[i], nums[i])
#    min_product[i] = min(min_product[i - 1] * nums[i], max_product[i - 1] * nums[i], nums[i])
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        N = len(nums)
        max_product = [0 for _ in range(N)]
        min_product = [0 for _ in range(N)]
        min_product[0] = max_product[0] = nums[0]
        ans = nums[0]
        for i in range(1, N):
            max_product[i] = max(min_product[i - 1] * nums[i], max_product[i - 1] * nums[i], nums[i])
            min_product[i] = min(min_product[i - 1] * nums[i], max_product[i - 1] * nums[i], nums[i])
            ans = max(ans, max_product[i])
        return ans

# DP optimization with O(1) space
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        pre_max = pre_min = ans = nums[0]
        for i in range(1, len(nums)):
            pre_max, pre_min = max(pre_min * nums[i], pre_max * nums[i], nums[i]), min(pre_min * nums[i], pre_max * nums[i], nums[i])
            ans = max(ans, pre_max)
        return ans


if __name__ == '__main__':
    S = Solution()
    print(S.maxProduct([-2, -1, -3]))
