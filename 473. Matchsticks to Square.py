# -*- coding: utf-8 -*-
# @Time    : 2018/12/21
# @Author  : qirui
# @FileName: 473. Matchsticks to Square.py

import numpy as np

#Time:O(4^N)
#Space:O(N)
#DFS (NP problem)
class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums: return False
        slide_length = sum(nums) // 4
        if slide_length * 4 != sum(nums):
            return False
        len_nums = len(nums)
        slide_sum = [0 for _ in range(4)]
        nums.sort(reverse=True)

        def dfs(index):
            if index == len_nums:
                return slide_sum[0] == slide_sum[1] == slide_sum[2] == slide_length
            for i in range(4):
                if slide_sum[i] + nums[index] <= slide_length:
                    slide_sum[i] += nums[index]
                    if dfs(index + 1):
                        return True
                    slide_sum[i] -= nums[index]
            return False

        return dfs(0)


#Time:O(4^N)
#Space:O(N)
#DFS + DP
class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums: return False
        slide_length = sum(nums) // 4
        if slide_length * 4 != sum(nums):
            return False
        len_nums = len(nums)
        slide_sum = [0 for _ in range(4)]
        nums.sort(reverse=True)

        def dfs(index):
            if index == len_nums:
                return slide_sum[0] == slide_sum[1] == slide_sum[2] == slide_length
            for i in range(4):
                if slide_sum[i] + nums[index] <= slide_length:
                    j = i - 1
                    while j > -1:
                        if slide_sum[i] == slide_sum[j]:
                            break
                        j -= 1
                    if j == -1:
                        slide_sum[i] += nums[index]
                        if dfs(index + 1):
                            return True
                        slide_sum[i] -= nums[index]
            return False

        return dfs(0)



if __name__ == '__main__':
    S = Solution()
    print(S.makesquare([1, 1, 2, 2, 2]))
