# -*- coding: utf-8 -*-
# @Time    : 2019/1/15
# @Author  : qirui
# @FileName: 773. Sliding Puzzle.py

import copy


# Time: O(N)
# Space: O(N)
# BFS
class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """

        if board == [[1, 2, 3], [4, 5, 0]]:
            return 0

        x, y = 0, 0
        for i in range(2):
            for j in range(3):
                if board[i][j] == 0:
                    x, y = i, j

        queue, visited = [(x, y, board, 0)], [board]
        while queue:
            x, y, state, level = queue.pop(0)
            for dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dir[0], y + dir[1]
                if 0 <= nx < 2 and 0 <= ny < 3:
                    next_state = copy.deepcopy(state)  # copy.copy(state)/state.copy() makes no sense
                    tmp = next_state[x][y]
                    next_state[x][y] = next_state[nx][ny]
                    next_state[nx][ny] = tmp
                    if next_state == [[1, 2, 3], [4, 5, 0]]:
                        return level + 1
                    if next_state not in visited:
                        visited.append(next_state)
                        queue.append((nx, ny, next_state, level + 1))
        return -1

# Time: O(N)
# Space: O(N)
# BFS by level
class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """

        if board == [[1, 2, 3], [4, 5, 0]]:
            return 0

        x, y = 0, 0
        for i in range(2):
            for j in range(3):
                if board[i][j] == 0:
                    x, y = i, j


        queue, visited, level = [(x, y, board)], [board], 0
        while queue:
            level += 1
            new_queue = []
            for x, y, state in queue:
                for dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dir[0], y + dir[1]
                    if 0 <= nx < 2 and 0 <= ny < 3:
                        next_state = copy.deepcopy(state)  # copy.copy(state)/state.copy() makes no sense
                        tmp = next_state[x][y]
                        next_state[x][y] = next_state[nx][ny]
                        next_state[nx][ny] = tmp
                        if next_state == [[1, 2, 3], [4, 5, 0]]:
                            return level
                        if next_state not in visited:
                            visited.append(next_state)
                            new_queue.append((nx, ny, next_state))
            queue = new_queue
        return -1

# Time: O(N)
# Space: O(N)
# BFS looks better
class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """

        [(x, y)] = [(i, j) for i in range(2) for j in range(3) if board[i][j] == 0]

        queue, visited = [(x, y, board, 0)], [board]
        while queue:
            x, y, state, level = queue.pop(0)
            if state == [[1, 2, 3], [4, 5, 0]]:
                return level
            for dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dir[0], y + dir[1]
                if 0 <= nx < 2 and 0 <= ny < 3:
                    next_state = copy.deepcopy(state)  # copy.copy(state)/state.copy() makes no sense
                    tmp = next_state[x][y]
                    next_state[x][y] = next_state[nx][ny]
                    next_state[nx][ny] = tmp
                    if next_state not in visited:
                        visited.append(next_state)
                        queue.append((nx, ny, next_state, level + 1))
        return -1


if __name__ == '__main__':
    S = Solution()
    print(S.slidingPuzzle([[1, 2, 3], [4, 0, 5]]))
