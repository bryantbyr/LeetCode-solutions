# -*- coding: utf-8 -*-
# @Time    : 2019/1/15
# @Author  : qirui
# @FileName: 675. Cut Off Trees for Golf Event.py

# Time: O(N^k)
# Space: O(N^2)
# BFS + heapq
class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """

        if not forest:
            return -1

        import heapq

        # heap, m, n = [], len(forest), len(forest[0])
        # for i in range(m):
        #     for j in range(n):
        #         if forest[i][j] > 1:
        #             heapq.heappush(heap, (forest[i][j], i, j))

        m, n = len(forest), len(forest[0])
        heap = [(forest[i][j], i, j) for i in range(m) for j in range(n) if forest[i][j] > 1]
        heapq.heapify(heap)

        def get_distance(x1, y1, x2, y2):
            if x1 == x2 and y1 == y2:
                return 0
            queue, dist, visited = [(x1, y1)], 0, {(x1, y1)}
            while queue:
                new_queue = []
                dist += 1
                for r, c in queue:
                    for dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr, nc = r + dir[0], c + dir[1]
                        if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited and forest[nr][nc] != 0:
                            visited.add((nr, nc))
                            if nr == x2 and nc == y2:
                                return dist
                            new_queue.append((nr, nc))
                queue = new_queue
            return -1

        res = 0
        x, y = 0, 0
        while heap:
            _, nx, ny = heapq.heappop(heap)
            dist = get_distance(x, y, nx, ny)
            if dist == -1:
                return -1
            res += dist
            x, y = nx, ny

        return res


if __name__ == '__main__':
    S = Solution()
    print(S.cutOffTree([
        [1, 2, 3],
        [0, 0, 4],
        [7, 6, 5]
    ]))
