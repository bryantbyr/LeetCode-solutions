# -*- coding: utf-8 -*-
# @Time    : 2019/1/12
# @Author  : qirui
# @FileName: 301. Remove Invalid Parentheses.py


# 115 / 126 test cases passed. Status: Time Limit Exceeded
# class Solution(object):
#     def removeInvalidParentheses(self, s):
#         """
#         :type s: str
#         :rtype: List[str]
#         """
#
#         def isvalid(pattern):
#             stack = []
#             for c in pattern:
#                 if c == '(':
#                     stack.append(c)
#                 elif c == ')':
#                     if not stack:
#                         return False
#                     stack.pop()
#             return len(stack) == 0
#
#         def dfs(index, tmp, cnt):
#             if cnt > self.min_cnt:
#                 return
#             if isvalid(tmp):
#                 self.min_cnt = cnt
#                 res.add(tmp.replace(" ", ""))
#                 return
#             if index > n - 1:
#                 return
#             dfs(index + 1, tmp, cnt)
#             dfs(index + 1, tmp[:index] + " " + tmp[index + 1:], cnt + 1)
#
#         n, res = len(s), set()
#         self.min_cnt = float('inf')
#         dfs(0, s, 0)
#         return list(res)

# Time: O(2^N)
# Space: O(N)
# DFS with optimization
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def isvalid(pattern):
            stack = []
            for c in pattern:
                if c == '(':
                    stack.append(c)
                elif c == ')':
                    if not stack:
                        return False
                    stack.pop()
            return len(stack) == 0

        def dfs(index, tmp, cnt):
            if cnt > self.min_cnt:
                return
            if isvalid(tmp):
                # if cnt < self.min_cnt:
                #     self.min_cnt = cnt
                #     res.clear()
                self.min_cnt = cnt
                res.add(tmp.replace(" ", ""))
                return
            if index > n - 1:
                return
            while tmp[index] != '(' and tmp[index] != ')':
                index += 1
                if index > n - 1:
                    return
            dfs(index + 1, tmp, cnt)
            dfs(index + 1, tmp[:index] + " " + tmp[index + 1:], cnt + 1)

        n, res, self.min_cnt = len(s), set(), float('inf')
        dfs(0, s, 0)
        return list(res)

# 64 / 126 test cases passed. Status: Time Limit Exceeded
# DFS
# class Solution(object):
#     def removeInvalidParentheses(self, s):
#         """
#         :type s: str
#         :rtype: List[str]
#         """
#
#         def isvalid(pattern):
#             stack = []
#             for c in pattern:
#                 if c == '(':
#                     stack.append(c)
#                 elif c == ')':
#                     if not stack:
#                         return False
#                     stack.pop()
#             return len(stack) == 0
#
#         def dfs(tmp, cnt):
#             if cnt > self.min_cnt:
#                 return
#             if isvalid(tmp):
#                 if cnt < self.min_cnt:
#                     self.min_cnt = cnt
#                     res.clear()
#                 res.add(tmp)
#                 return
#             for i in range(len(tmp)):
#                 if tmp[i] in ['(', ')']:
#                     dfs(tmp[:i] + tmp[i + 1:], cnt + 1)
#
#         res, self.min_cnt = set(), float('inf')
#         dfs(s, 0)
#         return list(res)


# Learn from discuss
# Time: O(N)
# Space:O(N)
# BFS
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def isvalid(pattern):
            cnt = 0
            for c in pattern:
                if c == '(':
                    cnt += 1
                elif c == ')':
                    if cnt <= 0:
                        return False
                    cnt -= 1
            return cnt == 0

        level = {s}
        # level = [s]
        while level:
            valid = list(filter(isvalid, level))
            if valid:
                return valid
            level = {s[:i] + s[i + 1:] for s in level for i in range(len(s))}
            # level = [s[:i] + s[i + 1:] for s in level for i in range(len(s))]


if __name__ == '__main__':
    S = Solution()
    s = ")((())))))()(((l(((("
    # s = ")((())))))()(((l("
    print(S.removeInvalidParentheses(s))
