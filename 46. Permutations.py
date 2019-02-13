# -*- coding: utf-8 -*-
# @Time    : 2019/2/12
# @Author  : qirui
# @FileName: 46. Permutations.py

# method #1
# Backtrack/DFS (general)
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def backtrack(tmp):
            if len(tmp) == N:
                res.append(tmp)
                return
            for i in range(N):
                if nums[i] in tmp:  continue
                backtrack(tmp + [nums[i]])

        N = len(nums)
        res = []
        backtrack([])
        return res

# method #2
# Backtrack/DFS
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def backtrack(tmp, list):
            if len(tmp) == N:
                res.append(tmp)
                return
            for num in list:
                index = list.index(num)
                list.remove(num)
                backtrack(tmp + [num], list)
                list.insert(index, num)

        N = len(nums)
        res = []
        backtrack([], nums)
        return res

# method #2 optimization #1
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def backtrack(tmp, list):
            if len(tmp) == N:
                res.append(tmp)
                return
            for i in range(len(list)):
                backtrack(tmp + [list[i]], list[:i] + list[i + 1:])

        N = len(nums)
        res = []
        backtrack([], nums)
        return res


# method #2 optimization #2
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def backtrack(tmp):
            if len(tmp) == N:
                res.append(tmp)
                return
            for num in set(nums) - set(tmp):
                backtrack(tmp + [num])

        N = len(nums)
        res = []
        backtrack([])
        return res


if __name__ == '__main__':
    S = Solution()
    print(S.permute([1, 2, 3]))
