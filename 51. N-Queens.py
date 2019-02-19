# -*- coding: utf-8 -*-
# @Time    : 2019/2/18
# @Author  : qirui
# @FileName: 51. N-Queens.py


# 6 / 9 test cases passed.  Status: Time Limit Exceeded
# Backtracking/DFS
# class Solution(object):
#     def solveNQueens(self, n):
#         """
#         :type n: int
#         :rtype: List[List[str]]
#         """
#
#         def isValid(board, row, col):
#             for i in range(n):
#                 if board[row][i] != '.' or board[i][col] != '.':
#                     return False
#             i, j = row - 1, col - 1
#             while i >= 0 and j >= 0:
#                 if board[i][j] != '.':    return False
#                 i -= 1
#                 j -= 1
#             i, j = row + 1, col + 1
#             while i < n and j < n:
#                 if board[i][j] != '.':    return False
#                 i += 1
#                 j += 1
#             i, j = row - 1, col + 1
#             while i >= 0 and j < n:
#                 if board[i][j] != '.':    return False
#                 i -= 1
#                 j += 1
#             i, j = row + 1, col - 1
#             while i < n and j >= 0:
#                 if board[i][j] != '.':    return False
#                 i += 1
#                 j -= 1
#             return True
#
#         def backtrack(board, cnt):
#             if cnt == 0:
#                 tmp = ["".join(row) for row in board]
#                 if tmp not in res:
#                     res.append(tmp)
#                 return
#
#             for i in range(n):
#                 for j in range(n):
#                     if board[i][j] == '.':
#                         if isValid(board, i, j):
#                             board[i][j] = 'Q'
#                             cnt -= 1
#                             backtrack(board, cnt)
#                             cnt += 1
#                             board[i][j] = '.'
#
#         board = [['.' for _ in range(n)] for _ in range(n)]
#         res = []
#         backtrack(board, n)
#         return res


# Backtracking/DFS
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        def isValid(board, row, col):
            for i in range(row):
                if board[i][col] != '.':
                    return False
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if board[i][j] != '.':    return False
                i -= 1
                j -= 1
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if board[i][j] != '.':    return False
                i -= 1
                j += 1
            return True

        def backtrack(board, row):
            if row == n:
                res.append(["".join(row) for row in board])
                return

            for j in range(n):
                if board[row][j] == '.' and isValid(board, row, j):
                    board[row][j] = 'Q'
                    backtrack(board, row + 1)
                    board[row][j] = '.'

        board = [['.' for _ in range(n)] for _ in range(n)]
        res = []
        backtrack(board, 0)
        return res


if __name__ == '__main__':
    S = Solution()
    ans = S.solveNQueens(7)
    print(ans)
    print(len(ans))
