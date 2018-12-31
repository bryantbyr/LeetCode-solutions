# -*- coding: utf-8 -*-
# @Time    : 2018/12/24
# @Author  : qirui
# @FileName: 638. Shopping Offers.py

import operator


# Learn from discuss
# DFS with memorization
class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """

        memo = {}
        special = list(filter(lambda x: operator.le(x[:-1], needs), special))

        def dfs(cur_needs):
            if tuple(cur_needs) in memo:
                return memo[tuple(cur_needs)]
            val = sum([p * n for p, n in zip(price, cur_needs)])
            for spe in special:
                if spe[-1] < val:
                    tmp = [need - sp for need, sp in zip(cur_needs, spe)]
                    if min(tmp) >= 0:
                        val = min(val, dfs(tmp) + spe[-1])
            memo[tuple(cur_needs)] = val
            return val

        return dfs(needs)


if __name__ == '__main__':
    S = Solution()
    print(S.shoppingOffers([1, 1, 1],
                           [[1, 1, 0, 0], [2, 2, 1, 9]],
                           [1, 1, 0]))
