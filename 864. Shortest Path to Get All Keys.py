# -*- coding: utf-8 -*-
# @Time    : 2019/1/19
# @Author  : qirui
# @FileName: 864. Shortest Path to Get All Keys.py


# Time: O(N^2)
# Space: O(N^2)
# BFS optimization using Bit Manipulation
class Solution(object):
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """

        m, n = len(grid), len(grid[0])
        start_x, start_y, final_state = 0, 0, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    start_x, start_y = i, j
                if 'a' <= grid[i][j] <= 'f':
                    final_state |= 1 << ord(grid[i][j]) - ord('a')

        queue, step, seen = [(start_x, start_y, 0)], 0, set([(start_x, start_y, 0)])
        while queue:
            step += 1
            new_queue = []
            for x, y, state in queue:
                for dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dir[0], y + dir[1]
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != "#":
                        if grid[nx][ny] in "abcdef":
                            next_state = state | 1 << ord(grid[nx][ny]) - ord('a')
                            if next_state == final_state:
                                return step
                            if (nx, ny, next_state) not in seen:
                                seen.add((nx, ny, next_state))
                                new_queue.append((nx, ny, next_state))
                        elif grid[nx][ny] not in "ABCDEF" or (1 << ord(grid[nx][ny]) - ord('A')) & state:
                            if (nx, ny, state) not in seen:
                                seen.add((nx, ny, state))
                                new_queue.append((nx, ny, state))
            queue = new_queue

        return -1


# Time: O(N^2)
# Space: O(N^2)
# BFS optimization using Bit Manipulation looks better
class Solution(object):
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """

        m, n = len(grid), len(grid[0])
        start_x, start_y, final_state = 0, 0, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    start_x, start_y = i, j
                elif grid[i][j] in "abcdef":
                    final_state |= 1 << ord(grid[i][j]) - ord('a')

        queue, step, seen = [(start_x, start_y, 0)], 0, set([(start_x, start_y, 0)])
        while queue:
            new_queue = []
            for x, y, state in queue:
                if state == final_state:
                    return step
                for dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dir[0], y + dir[1]
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != "#":
                        if grid[nx][ny] in "ABCDEF" and not (1 << ord(grid[nx][ny]) - ord('A')) & state:
                            continue
                        next_state = state | 1 << ord(grid[nx][ny]) - ord('a') if grid[nx][ny] in "abcdef" else state
                        if (nx, ny, next_state) not in seen:
                            seen.add((nx, ny, next_state))
                            new_queue.append((nx, ny, next_state))

            step += 1
            queue = new_queue

        return -1

# Time: O(N^2)
# Space: O(N^2)
# BFS optimization using Bit Manipulation looks better with a little improvement
class Solution(object):
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """

        m, n = len(grid), len(grid[0])
        start_x, start_y, final_state = 0, 0, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    start_x, start_y = i, j
                elif grid[i][j] in "abcdef":
                    final_state |= 1 << ord(grid[i][j]) - ord('a')

        queue, step, seen = [(start_x, start_y, 0)], 0, set([(start_x, start_y, 0)])
        while queue:
            new_queue = []
            for x, y, state in queue:
                if state == final_state:
                    return step
                for dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dir[0], y + dir[1]
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != "#":
                        if grid[nx][ny] not in "ABCDEF" or (1 << ord(grid[nx][ny]) - ord('A')) & state:
                            if (nx, ny, state) not in seen:
                                next_state = state | 1 << ord(grid[nx][ny]) - ord('a') if grid[nx][ny] in "abcdef" else state
                                seen.add((nx, ny, next_state))
                                new_queue.append((nx, ny, next_state))

            step += 1
            queue = new_queue

        return -1


if __name__ == '__main__':
    S = Solution()
    print(S.shortestPathAllKeys(["@...a", ".###A", "b.BCc"]))
