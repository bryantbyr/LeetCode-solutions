# 130. Surrounded Regions

#Learn from discuss on 20181207
#Time:O(N^3)
#Space:O(N)
#DFS
class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0]) if m > 0 else 0

        def dfs(x, y):
            if x < 0 or x > m - 1 or y < 0 or y > n - 1 or board[x][y] != 'O':
                return
            board[x][y] = '1'
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)

        for x in range(m):
            dfs(x, 0)
            if n > 1:
                dfs(x, n - 1)

        for y in range(1, n - 1):
            dfs(0, y)
            if m - 1 > 0:
                dfs(m - 1, y)

        for x in range(m):
            for y in range(n):
                if board[x][y] == 'O':
                    board[x][y] = 'X'

        for x in range(m):
            for y in range(n):
                if board[x][y] == '1':
                    board[x][y] = 'O'


if __name__ == '__main__':
    S = Solution()
    list = [["O", "O"], ["O", "O"]]
    S.solve(list)
    print(list)
