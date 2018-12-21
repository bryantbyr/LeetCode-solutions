# -*- coding: utf-8 -*-
# @Time    : 2018/12/20
# @Author  : qirui
# @FileName: 417. Pacific Atlantic Water Flow.py

# Time:O(N)
# Space:O(N)
# DFS in matrix + DP (using two visited matrixes)
class Solution:
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        m,n = len(matrix),0
        if m>0:
            n = len(matrix[0])

        def dfs(x,y,visited):
            if visited[x][y]:
                return
            visited[x][y] = True
            for direction in [(0,1),(0,-1),(1,0),(-1,0)]:
                i,j = x+direction[0],y+direction[1]
                if i>=0 and i<m and j>=0 and j<n and matrix[x][y] <= matrix[i][j]:
                    dfs(i,j,visited)

        p_visited = [[False for _ in range(n)] for _ in range(m)]
        a_visited = [[False for _ in range(n)] for _ in range(m)]

        for i in range(m):
            dfs(i,0,p_visited)
            dfs(i,n-1,a_visited)
        for j in range(n):
            dfs(0,j,p_visited)
            dfs(m-1,j,a_visited)

        ans = []
        for i in range(m):
            for j in range(n):
                if p_visited[i][j] and a_visited[i][j]:
                    ans.append([i,j])
        return ans

if __name__=='__main__':
    S = Solution()
    print(S.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
