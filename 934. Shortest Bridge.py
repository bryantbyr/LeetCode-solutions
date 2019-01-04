# -*- coding: utf-8 -*-
# @Time    : 2019/1/3
# @Author  : qirui
# @FileName: 934. Shortest Bridge.py


# Learn from discuss
# Time:O(N)
# Space:O(N)
# BFS
class Solution:
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """

        def dfs(x, y):
            queue.append((x, y))
            A[x][y] = -1
            for i, j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= i < n and 0 <= j < n and A[i][j] == 1:
                    dfs(i, j)

        def find_first():
            for i in range(n):
                for j in range(n):
                    if A[i][j]:
                        return i, j

        n, queue, res = len(A), [], 0
        dfs(*find_first())
        while queue:
            count = len(queue)
            while count > 0:
                r, c = queue.pop(0)
                for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    if 0 <= nr < n and 0 <= nc < n:
                        if not A[nr][nc]:
                            A[nr][nc] = -1
                            queue.append((nr, nc))
                        elif A[nr][nc] == 1:
                            return res
                count -= 1
            res += 1

# Learn from discuss
# Time:O(N)
# Space:O(N)
# BFS
class Solution:
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """

        def dfs(x, y):
            queue.append((x, y))
            A[x][y] = -1
            for i, j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= i < n and 0 <= j < n and A[i][j] == 1:
                    dfs(i, j)

        def find_first():
            for i in range(n):
                for j in range(n):
                    if A[i][j]:
                        return i, j

        n, queue, res = len(A), [], 0
        dfs(*find_first())
        pre = len(queue)
        while True:
            cur = 0
            while pre > 0:
                r, c = queue.pop(0)
                for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    if 0 <= nr < n and 0 <= nc < n:
                        if not A[nr][nc]:
                            A[nr][nc] = -1
                            queue.append((nr, nc))
                            cur += 1
                        elif A[nr][nc] == 1:
                            return res
                pre -= 1
            pre = cur
            res += 1


if __name__ == '__main__':
    S = Solution()
    print(S.shortestBridge([[0, 1, 0], [0, 0, 0], [0, 0, 1]]))
