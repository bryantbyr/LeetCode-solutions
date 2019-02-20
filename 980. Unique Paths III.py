# -*- coding: utf-8 -*-
# @Time    : 2019/2/19
# @Author  : qirui
# @FileName: 980. Unique Paths III.py

# Backtracking/DFS using extra set
class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def backtrack(row, col, cnt):
            for dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = row + dir[0], col + dir[1]
                if 0 <= nr < m and 0 <= nc < n:
                    if grid[nr][nc] == 2:
                        if cnt == 0:
                            self.ans += 1
                            return
                        else:
                            continue
                    if grid[nr][nc] == 0 and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        backtrack(nr, nc, cnt - 1)
                        visited.remove((nr, nc))

        m, n = len(grid), len(grid[0])
        start_r, start_c = 0, 0
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start_r, start_c = i, j
                elif grid[i][j] == 0:
                    cnt += 1
        self.ans = 0
        visited = set()
        backtrack(start_r, start_c, cnt)
        return self.ans


# Backtracking/DFS not using extra set
class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def backtrack(row, col, cnt):
            for dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = row + dir[0], col + dir[1]
                if 0 <= nr < m and 0 <= nc < n:
                    if grid[nr][nc] == 2:
                        if cnt == 0:
                            self.ans += 1
                            return
                        else:
                            continue  # find the next direction from (row,col)
                    if grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        backtrack(nr, nc, cnt - 1)
                        grid[nr][nc] = 0

        m, n = len(grid), len(grid[0])
        start_r, start_c = 0, 0
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start_r, start_c = i, j
                elif grid[i][j] == 0:
                    cnt += 1
        self.ans = 0
        backtrack(start_r, start_c, cnt)
        return self.ans


if __name__ == '__main__':
    S = Solution()
    print(S.uniquePathsIII([[1, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 2, -1]]))
