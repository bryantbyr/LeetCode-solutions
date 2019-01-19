# -*- coding: utf-8 -*-
# @Time    : 2019/1/17
# @Author  : qirui
# @FileName: 815. Bus Routes.py


import collections


# 44 / 45 test cases passed.    Status: Time Limit Exceeded
# class Solution(object):
#     def numBusesToDestination(self, routes, S, T):
#         """
#         :type routes: List[List[int]]
#         :type S: int
#         :type T: int
#         :rtype: int
#         """
#
#         if S == T:
#             return 0
#
#         dict = collections.defaultdict(list)
#         for route in routes:
#             for stop in route:
#                 dict[stop].append(route)
#
#         queue, seen = [(item, 1) for item in dict[S]], dict[S]
#         while queue:
#             bus, num = queue.pop(0)
#             if T in bus:
#                 return num
#             for stop in bus:
#                 for nei in dict[stop]:
#                     if nei not in seen:
#                         seen.append(nei)
#                         queue.append((nei, num + 1))
#         return -1


# 44 / 45 test cases passed.    Status: Time Limit Exceeded
# class Solution(object):
#     def numBusesToDestination(self, routes, S, T):
#         """
#         :type routes: List[List[int]]
#         :type S: int
#         :type T: int
#         :rtype: int
#         """
#
#         if S == T:
#             return 0
#
#         dict = collections.defaultdict(list)
#         routes = list(map(tuple,routes))
#         for route in routes:
#             for stop in route:
#                 dict[stop].append(route)
#
#         queue, seen = [(item, 1) for item in dict[S]], set(dict[S])
#         while queue:
#             bus, num = queue.pop(0)
#             if T in bus:
#                 return num
#             for stop in bus:
#                 for nei in dict[stop]:
#                     if nei not in seen:
#                         seen.add(nei)
#                         queue.append((nei, num + 1))
#         return -1

# 44 / 45 test cases passed.   Status: Time Limit Exceeded
# class Solution(object):
#     def numBusesToDestination(self, routes, S, T):
#         """
#         :type routes: List[List[int]]
#         :type S: int
#         :type T: int
#         :rtype: int
#         """
#
#         dict = collections.defaultdict(list)
#         for route in routes:
#             for stop in route:
#                 dict[stop].append(route)
#
#         queue, seen = [(S, 0)], set([S])
#         while queue:
#             bus, num = queue.pop(0)
#             if bus == T:
#                 return num
#             for root in dict[bus]:
#                 for nei in root:
#                     if nei not in seen:
#                         seen.add(nei)
#                         queue.append((nei, num + 1))
#         return -1


# 44 / 45 test cases passed.   Status: Time Limit Exceeded
# class Solution(object):
#     def numBusesToDestination(self, routes, S, T):
#         """
#         :type routes: List[List[int]]
#         :type S: int
#         :type T: int
#         :rtype: int
#         """
#
#         if S == T:
#             return 0
#
#         dict = collections.defaultdict(list)
#         routes = list(map(tuple, routes))
#         for route in routes:
#             for stop in route:
#                 dict[stop].append(route)
#
#         queue, seen = [(item, 1) for item in dict[S]], set(dict[S])
#         while queue:
#             bus, num = queue.pop(0)
#             if T in bus:
#                 return num
#             for stop in bus:
#                 for nei in dict[stop]:
#                     if nei not in seen:
#                         seen.add(nei)
#                         queue.append((nei, num + 1))
#                 dict[stop] = []
#         return -1


# Learn from discuss
# Time: O(N)
# Space: O(N)
# BFS (notice the optimization to reduce the times of repeat visiting)
class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """

        dict = collections.defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                dict[stop].append(i)

        queue, seen = [(S, 0)], set([S])
        while queue:
            bus, num = queue.pop(0)
            if bus == T:
                return num
            for index in dict[bus]:
                for nei in routes[index]:
                    if nei not in seen:
                        seen.add(nei)
                        queue.append((nei, num + 1))
                routes[index] = []
        return -1


# my BFS optimization
class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """

        if S == T:
            return 0

        dict = collections.defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                dict[stop].append(i)

        queue = []
        for index in dict[S]:
            nei = routes[index][:]
            if nei:
                nei.remove(S)   # not to visit the same stop (the same next buses)
                queue.append((nei, 1))
                routes[index] = []  # not to visit the same bus

        while queue:
            bus, num = queue.pop(0)
            if T in bus:
                return num
            for stop in bus:
                for index in dict[stop]:
                    nei = routes[index][:]
                    if nei:
                        nei.remove(stop)    # not to visit the same stop (the same next buses)
                        queue.append((nei, num + 1))
                        routes[index] = []  # not to visit the same bus

        return -1

# my BFS optimization
class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """

        if S == T:
            return 0

        dict = collections.defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                dict[stop].append(i)
        queue = []
        for index in dict[S]:
            nei = routes[index][:]
            if nei:
                queue.append((nei, 1))
                routes[index] = []  # not to visit the same bus
        dict[S] = []

        while queue:
            bus, num = queue.pop(0)
            if T in bus:
                return num
            for stop in bus:
                for index in dict[stop]:
                    nei = routes[index][:]
                    if nei:
                        queue.append((nei, num + 1))
                        routes[index] = []  # not to visit the same bus
                dict[stop] = []
        return -1

# 44 / 45 test cases passed.   Status: Time Limit Exceeded
# class Solution(object):
#     def numBusesToDestination(self, routes, S, T):
#         """
#         :type routes: List[List[int]]
#         :type S: int
#         :type T: int
#         :rtype: int
#         """
#
#         if S == T:
#             return 0
#
#         dict = collections.defaultdict(list)
#         for i, route in enumerate(routes):
#             for stop in route:
#                 dict[stop].append(i)
#         queue = []
#         for index in dict[S]:
#             queue.append((routes[index][:], 1))
#         dict[S] = []
#
#         while queue:
#             bus, num = queue.pop(0)
#             if T in bus:
#                 return num
#             for stop in bus:
#                 for index in dict[stop]:
#                     queue.append((routes[index], num + 1))
#                 dict[stop] = []
#         return -1



if __name__ == '__main__':
    S = Solution()
    routes = [[1, 2, 7], [3, 6, 7]]
    s = 1
    T = 6
    print(S.numBusesToDestination(routes, s, T))
