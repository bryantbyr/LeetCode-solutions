# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# created on 20170809
# 列表生成式+"DP"+逆序string


class Solution(object):
    def isPlaindromic(self,s):
        # if s==s[::-1]:
        #     return 1
        # else:
        #     return 0
        return s==s[::-1]

    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=len(s)
        dp=[[]for i in range(l+1)]
        dp[0]=0
        for i in range(1,l+1):
            dp[i] = dp[i-1]+sum(self.isPlaindromic(s[j:i]) for j in range(i))
        return dp[l]

s = Solution()
print(s.countSubstrings("aba"))
