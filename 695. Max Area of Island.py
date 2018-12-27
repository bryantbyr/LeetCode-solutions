# -*- coding: utf-8 -*-
# @Time    : 2018/12/24
# @Author  : qirui
# @FileName: 695. Max Area of Island.py

# Time:O(N^2)
# Space:(N^2)
# standard matrix DFS matrix visited
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def dfs(x, y):
            visited[x][y] = True
            self.tmp += 1
            for dir in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                i, j = x + dir[0], y + dir[1]
                if 0 <= i < m and 0 <= j < n and grid[i][j] != 0 and not visited[i][j]:
                    dfs(i, j)

        m, ans = len(grid), 0
        n = len(grid[0]) if m > 0 else 0
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0 and not visited[i][j]:
                    self.tmp = 0
                    dfs(i, j)
                    ans = max(ans, self.tmp)
        return ans


# Time:O(N^2)
# Space:(N^2)
# standard matrix DFS using list visited
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def dfs(x, y):
            visited.append((x, y))
            self.tmp += 1
            for dir in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                i, j = x + dir[0], y + dir[1]
                if 0 <= i < m and 0 <= j < n and grid[i][j] != 0 and (i, j) not in visited:
                    dfs(i, j)

        m, ans = len(grid), 0
        n = len(grid[0]) if m > 0 else 0
        visited = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0 and (i, j) not in visited:
                    self.tmp = 0
                    dfs(i, j)
                    ans = max(ans, self.tmp)
        return ans

# Learn from discuss
# Time:O(N^2)
# Space:(N^2)
# standard matrix DFS not using visited
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def dfs(x, y):
            grid[x][y] = 0
            self.tmp += 1
            for dir in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                i, j = x + dir[0], y + dir[1]
                if 0 <= i < m and 0 <= j < n and grid[i][j] != 0:
                    dfs(i, j)

        m, ans = len(grid), 0
        n = len(grid[0]) if m > 0 else 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    self.tmp = 0
                    dfs(i, j)
                    ans = max(ans, self.tmp)
        return ans

# Learn from discuss
# Time:O(N^2)
# Space:(N^2)
# standard matrix DFS with returned value
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def dfs(x, y):
            if x < 0 or x > m - 1 or y < 0 or y > n - 1 or grid[x][y] == 0:
                return 0
            grid[x][y] = 0
            return 1 + dfs(x - 1, y) + dfs(x + 1, y) + dfs(x, y - 1) + dfs(x, y + 1)

        m, ans = len(grid), 0
        n = len(grid[0]) if m > 0 else 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    ans = max(ans, dfs(i, j))
        return ans


if __name__ == '__main__':
    S = Solution()
    print(S.maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                             [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                             [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))
