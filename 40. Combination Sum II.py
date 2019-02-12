# -*- coding: utf-8 -*-
# @Time    : 2019/1/28
# @Author  : qirui
# @FileName: 40. Combination Sum II.py

# 122 / 172 test cases passed.  Status: Time Limit Exceeded
# class Solution(object):
#     def combinationSum2(self, candidates, target):
#         """
#         :type candidates: List[int]
#         :type target: int
#         :rtype: List[List[int]]
#         """
#
#         def dfs(index, tmp, sum):
#             if sum == target:
#                 new_permutation = sorted(tmp)
#                 if new_permutation not in res:
#                     res.append(new_permutation)
#                 return
#             if index == N:
#                 return
#             dfs(index + 1, tmp + [candidates[index]], sum + candidates[index])
#             dfs(index + 1, tmp, sum)
#
#         N = len(candidates)
#         res = []
#         dfs(0, [], 0)
#         return res

# Learn from discuss
# A new way for recursion
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def dfs(cur_index, tmp, sum):
            if sum == target:
                # res.append(tmp)
                res.append(tmp[:])
                return
            elif sum > target:
                return
            for i in range(cur_index, N):
                if i > cur_index and candidates[i] == candidates[i - 1]:  continue
                # dfs(i + 1, tmp + [candidates[i]], sum + candidates[i])
                tmp.append(candidates[i])
                dfs(i + 1, tmp, sum + candidates[i])
                tmp.remove(candidates[i])

        candidates.sort()
        N = len(candidates)
        res = []
        dfs(0, [], 0)
        return res


if __name__ == '__main__':
    S = Solution()
    candidates = [2, 3, 1, 4]
    target = 10
    print(S.combinationSum2(candidates, target))
