# -*- coding: utf-8 -*-
# @Time    : 2019/2/18
# @Author  : qirui
# @FileName: 52. N-Queens II.py


class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """

        def isValid(board, row, col):
            for i in range(row):
                if board[i][col] != '.':    return False
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if board[i][j] != '.':  return False
                i -= 1
                j -= 1
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if board[i][j] != '.':  return False
                i -= 1
                j += 1
            return True

        def backtrack(board, row):
            if row == n:
                self.ans += 1
                return
            for j in range(n):
                if board[row][j] == '.' and isValid(board, row, j):
                    board[row][j] = 'Q'
                    backtrack(board, row + 1)
                    board[row][j] = '.'

        board = [['.' for _ in range(n)] for _ in range(n)]
        self.ans = 0
        backtrack(board, 0)
        return self.ans


if __name__ == '__main__':
    S = Solution()
    print(S.totalNQueens(4))
