# -*- coding: utf-8 -*-
# @Time    : 2019/2/15
# @Author  : qirui
# @FileName: 60. Permutation Sequence.py

# 188 / 200 test cases passed.  Status: Time Limit Exceeded
# Backtrack/DFS (general)
# class Solution(object):
#     def getPermutation(self, n, k):
#         """
#         :type n: int
#         :type k: int
#         :rtype: str
#         """
#
#         def backtrack(tmp):
#             if len(tmp) == n:
#                 res.append(tmp)
#                 return
#             for i in range(1, n + 1):
#                 if str(i) in tmp:   continue
#                 if len(res) < k:
#                     backtrack(tmp + str(i))
#
#         res = []
#         backtrack("")
#         return res[k - 1]


# refernce: https://leetcode.com/problems/permutation-sequence/discuss/22512/Share-my-Python-solution-with-detailed-explanation
# math
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        import math

        nums = [i for i in range(1, n + 1)]
        res = ""
        k -= 1
        while n > 0:
            n -= 1
            index, k = divmod(k, math.factorial(n))
            res += str(nums[index])
            nums.remove(nums[index])
        return res


if __name__ == '__main__':
    S = Solution()
    print(S.getPermutation(3, 6))
