# -*- coding: utf-8 -*-
# @Time    : 2018/12/22
# @Author  : qirui
# @FileName: 698. Partition to K Equal Sum Subsets.py

#Time:O(k^N)
#Space:O(N)
#DFS (NP problem)
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        def dfs(index):
            if index < 0:
                return True
            for i in range(k):
                if slide_sum[i] + nums[index] <= slide:
                    slide_sum[i] += nums[index]
                    if dfs(index - 1):
                        return True
                    slide_sum[i] -= nums[index]
            return False

        if not nums: return False
        slide = sum(nums) // k
        if slide * k != sum(nums): return False
        slide_sum = [0] * k
        nums.sort()
        return dfs(len(nums) - 1)

#Time:O(k^N)
#Space:O(N)
#DFS + DP
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        def dfs(index):
            if index < 0:
                return True
            for i in range(k):
                if slide_sum[i] >= nums[index]:
                    j = i - 1
                    while j > -1:
                        if slide_sum[i] == slide_sum[j]:
                            break
                        j -= 1
                    if j == -1:
                        slide_sum[i] -= nums[index]
                        if dfs(index - 1):
                            return True
                        slide_sum[i] += nums[index]
            return False

        if not nums: return False
        slide = sum(nums) // k
        if slide * k != sum(nums): return False
        slide_sum = [slide] * k
        nums.sort()
        return dfs(len(nums) - 1)

#Time:O(N^k)
#Space:O(N)
#Time Limit Exceeded
# class Solution(object):
#     def canPartitionKSubsets(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: bool
#         """
#
#         def dfs(cur_sum, k):
#             if k == 0:
#                 return True
#             if cur_sum == target:
#                 return dfs(0, k - 1)
#
#             for i in range(length):
#                 if not visited[i] and cur_sum + nums[i] <= target:
#                     visited[i] = True
#                     if dfs(cur_sum + nums[i], k):
#                         return True
#                     visited[i] = False
#             return False
#
#         if not nums: return False
#         target = sum(nums) // k
#         if target * k != sum(nums): return False
#         length = len(nums)
#         visited = [False] * length
#         nums.sort(reverse=True)
#         return dfs(0, k)


if __name__ == '__main__':
    S = Solution()
    print(S.canPartitionKSubsets([85, 35, 40, 64, 86, 45, 63, 16, 5364, 110, 5653, 97, 95], 7))
