# -*- coding: utf-8 -*-
# @Time    : 2019/1/14
# @Author  : qirui
# @FileName: 529. Minesweeper.py

# Time: O(N)
# Space: O(N)
# DFS
class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """

        def dfs(r, c):
            if board[r][c] != 'E' and board[r][c] != 'M':
                return

            if board[r][c] == 'M':
                board[r][c] = 'X'
                return

            cnt = 0
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
            for dir in directions:
                nr, nc = r + dir[0], c + dir[1]
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'M':
                    cnt += 1
            if cnt > 0:
                board[r][c] = str(cnt)
                return

            board[r][c] = 'B'
            for dir in directions:
                nr, nc = r + dir[0], c + dir[1]
                if 0 <= nr < m and 0 <= nc < n:
                    dfs(nr, nc)

        m, n = len(board), len(board[0])
        dfs(click[0], click[1])
        return board

# Time: O(N)
# Space: O(N)
# BFS
class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        m, n = len(board), len(board[0])
        queue = [(click[0], click[1])]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        while queue:
            r, c = queue.pop(0)
            if board[r][c] == 'M':
                board[r][c] = 'X'
                break
            if board[r][c] != 'E':
                continue
            new_queue, cnt = [], 0
            for dir in directions:
                nr, nc = r + dir[0], c + dir[1]
                if 0 <= nr < m and 0 <= nc < n:
                    if board[nr][nc] == 'M':
                        cnt += 1
                    new_queue.append((nr, nc))
            if cnt > 0:
                board[r][c] = str(cnt)
            else:
                board[r][c] = 'B'
                queue.extend(new_queue)

        return board


if __name__ == '__main__':
    S = Solution()
    print(S.updateBoard([['E', 'E', 'E', 'E', 'E'],
                         ['E', 'E', 'M', 'E', 'E'],
                         ['E', 'E', 'E', 'E', 'E'],
                         ['E', 'E', 'E', 'E', 'E']], [3, 0]))
