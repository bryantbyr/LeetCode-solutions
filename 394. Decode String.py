# -*- coding: utf-8 -*-
# @Time    : 2018/12/19
# @Author  : qirui
# @FileName: 394. Decode String.py

# Time:O(N^2)
# Space:O(N)
# DFS/Recursion
class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        if s == "":
            return ""

        if '0' < s[0] and s[0] <= '9':
            stack, start,end = ['['], s.index('[')+1,s.index('[')+1
            while stack:
                if s[end] == '[':
                    stack.append('[')
                elif s[end] == ']':
                    stack.pop()
                end += 1
            return self.decodeString(s[start:end - 1]) * int(s[0:start-1]) + self.decodeString(s[end:])
        else:
            return s[0] + self.decodeString(s[1:])


if __name__ == '__main__':
    S = Solution()
    print(S.decodeString("100[leetcode]"))
