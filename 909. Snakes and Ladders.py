# -*- coding: utf-8 -*-
# @Time    : 2019/1/20
# @Author  : qirui
# @FileName: 909. Snakes and Ladders.py


# standard BFS
class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """

        N = len(board)
        board_lst, cnt, dir = [0 for _ in range(N * N + 1)], 1, 1
        for i in range(N - 1, -1, -1):
            for j in range(N):
                board_lst[cnt] = board[i][(N - 1) * (dir == -1) + dir * j]
                cnt += 1
            dir = -dir

        queue, level, seen = [1], 0, set([1])
        while queue:
            level += 1
            new_queue = []
            for pos in queue:
                for i in range(6):
                    next_pos = board_lst[pos + 1 + i] if board_lst[pos + 1 + i] != -1 else pos + 1 + i
                    if next_pos == N * N:
                        return level
                    if next_pos not in seen:
                        seen.add(next_pos)
                        new_queue.append(next_pos)
            queue = new_queue

        return -1


if __name__ == '__main__':
    S = Solution()
    print(S.snakesAndLadders([[-1, 1, 2, -1],
                              [2, 13, 15, -1],
                              [-1, 10, -1, -1],
                              [-1, 6, 2, 8]]))
