# -*- coding: utf-8 -*-
# @Time    : 2019/2/18
# @Author  : qirui
# @FileName: 37. Sudoku Solver.py

# reference:    https://leetcode.com/problems/sudoku-solver/discuss/15752/Straight-Forward-Java-Solution-Using-Backtracking
# Backtracking*/DFS/Recursion
# 好题, 考察Backtracking/DFS思想
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        def isValid(board, i, j, item):
            for k in range(9):
                if board[i][k] != '.' and board[i][k] == item:  return False
                if board[k][j] != '.' and board[k][j] == item:  return False
                if board[3 * (i // 3) + k // 3][3 * (j // 3) + k % 3] != '.' and board[3 * (i // 3) + k // 3][
                    3 * (j // 3) + k % 3] == item:  return False
            return True

        def backtrack(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for num in range(1, 10):
                            if isValid(board, i, j, str(num)):
                                board[i][j] = str(num)
                                if backtrack(board):
                                    return True
                                board[i][j] = '.'
                        return False
            return True

        backtrack(board)


if __name__ == '__main__':
    S = Solution()
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    S.solveSudoku(board)
    print(board)
