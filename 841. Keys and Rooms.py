# -*- coding: utf-8 -*-
# @Time    : 2019/1/3
# @Author  : qirui
# @FileName: 841. Keys and Rooms.py

# Time: O(N)
# Space: O(N)
# DFS
class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """

        def dfs(v):
            if v in seen:
                return
            seen.add(v)
            for nei in rooms[v]:
                dfs(nei)

        seen = set()
        dfs(0)
        return len(seen) == len(rooms)

# Time: O(N)
# Space: O(N)
# DFS
class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """

        def dfs(v):
            seen.add(v)
            for nei in rooms[v]:
                if nei not in seen:
                    dfs(nei)

        seen = set()
        dfs(0)
        return len(seen) == len(rooms)


if __name__ == '__main__':
    S = Solution()
    print(S.canVisitAllRooms([[1], [2], [3], []]))
