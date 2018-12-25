# -*- coding: utf-8 -*-
# @Time    : 2018/12/24
# @Author  : qirui
# @FileName: 547. Friend Circles.py

# Time: O(N)
# Space:O(N)
# DFS
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """

        n = len(M)
        if n == 0: return 0
        visited, ans = [False for _ in range(n)], 0

        def dfs(index):
            if visited[index]:  return
            visited[index] = True
            for x in range(n):
                if M[index][x] == 1:
                    dfs(x)

        for i in range(n):
            if not visited[i]:
                dfs(i)
                ans += 1

        return ans


if __name__ == '__main__':
    S = Solution()
    print(S.findCircleNum([[1, 1, 0],
                           [1, 1, 1],
                           [0, 1, 1]]))
