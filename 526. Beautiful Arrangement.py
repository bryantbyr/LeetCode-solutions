# -*- coding: utf-8 -*-
# @Time    : 2019/2/17
# @Author  : qirui
# @FileName: 526. Beautiful Arrangement.py

# Backtracking/DFS (general)
class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """

        def backtrack(tmp, pos):
            if len(tmp) == N:
                self.ans += 1
                return
            for i in range(1, N + 1):
                if i in tmp:    continue
                if i % pos == 0 or pos % i == 0:
                    backtrack(tmp + [i], pos + 1)

            # if pos == N + 1:
            #     self.ans += 1
            #     return
            # for i in range(1, N + 1):
            #     if i in tmp or (i % pos != 0 and pos % i != 0):    continue
            #     backtrack(tmp + [i], pos + 1)

            # if pos == N + 1:
            #     self.ans += 1
            #     return
            # for i in range(1, N + 1):
            #     if i in tmp:    continue
            #     if i % pos == 0 or pos % i == 0:
            #         tmp.append(i)
            #         backtrack(tmp, pos + 1)
            #         tmp.remove(i)

        self.ans = 0
        backtrack([], 1)
        return self.ans


if __name__ == '__main__':
    S = Solution()
    print(S.countArrangement(4))
