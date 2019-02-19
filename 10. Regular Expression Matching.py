# -*- coding: utf-8 -*-
# @Time    : 2019/2/18
# @Author  : qirui
# @FileName: 10. Regular Expression Matching.py

# reference:    https://leetcode.com/problems/regular-expression-matching/solution/
# Backtracking/Recursion*
# 此题不难定位到Backtracking/DFS/Recursion, 耐心寻找递归(回溯)条件即如何递归是解决本问题的关键, 递归的终止条件的判定也具有一定技巧性
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        if not s:
            # if len(p) % 2 != 0:
            #     return False
            # for i in range(1, len(p), 2):
            #     if p[i] != '*':
            #         return False
            # return True
            for i in range(1, len(p), 2):
                if p[i] != '*':
                    return False
            return len(p) % 2 == 0

        first_match = p != "" and (p[0] == s[0] or p[0] == '.')

        # if not p:
        #     return not s
        # first_match = s != "" and (p[0] == s[0] or p[0] == '.')

        if len(p) > 1 and p[1] == "*":
            return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))
        else:
            return first_match and self.isMatch(s[1:], p[1:])


if __name__ == '__main__':
    S = Solution()
    print(S.isMatch("ab", ".*"))
