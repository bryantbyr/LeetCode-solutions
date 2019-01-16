# -*- coding: utf-8 -*-
# @Time    : 2019/1/14
# @Author  : qirui
# @FileName: 407. Trapping Rain Water II.py


# Learn from discuss
# Time: O(N^2)
# Space: O(N^2)
# Heap + BFS
class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """

        if not heightMap:
            return 0

        import heapq

        heap, m, n = [], len(heightMap), len(heightMap[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            heapq.heappush(heap, (heightMap[i][0], i, 0))
            heapq.heappush(heap, (heightMap[i][n - 1], i, n - 1))
            visited[i][0], visited[i][n - 1] = 1, 1
        for j in range(1, n - 1):
            heapq.heappush(heap, (heightMap[0][j], 0, j))
            heapq.heappush(heap, (heightMap[m - 1][j], m - 1, j))
            visited[0][j], visited[m - 1][j] = 1, 1

        res = 0
        while heap:
            height, x, y = heapq.heappop(heap)
            for dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dir[0], y + dir[1]
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    if heightMap[nx][ny] < height:
                        res += height - heightMap[nx][ny]
                        heapq.heappush(heap, (height, nx, ny))
                    else:
                        heapq.heappush(heap, (heightMap[nx][ny], nx, ny))
        return res


if __name__ == '__main__':
    S = Solution()
    print(S.trapRainWater([
        [1, 4, 3, 1, 3, 2],
        [3, 2, 1, 3, 2, 4],
        [2, 3, 3, 2, 3, 1]
    ]))
