# -*- coding: utf-8 -*-
# @Time    : 2019/2/15
# @Author  : qirui
# @FileName: 357. Count Numbers with Unique Digits.py


# Math
# Time: O(1)
# Space: O(1)
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """

        # if n == 0:
        #     return 1
        # if n == 1:
        #     return 10
        #
        # if n > 10:
        #     n = 10
        # ans = 10
        # for i in range(2, n + 1):
        #     tmp = 9
        #     for j in range(2, i + 1):
        #         tmp = tmp * (9 - j + 2)
        #     ans += tmp
        # return ans

        # if n == 0:
        #     return 1
        #
        # if n > 10:
        #     n = 10
        # ans = 1
        # for i in range(1, n + 1):
        #     tmp = 9
        #     if i > 1:
        #         for j in range(2, i + 1):
        #             tmp = tmp * (9 - j + 2)
        #     ans += tmp
        # return ans

        if n == 0:
            return 1
        if n == 1:
            return 10

        if n > 10:
            n = 10
        ans, tmp = 10, 9
        for i in range(2, n + 1):
            tmp *= (9 - i + 2)
            ans += tmp
        return ans


if __name__ == '__main__':
    S = Solution()
    print(S.countNumbersWithUniqueDigits(17))
