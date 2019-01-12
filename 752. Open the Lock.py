# -*- coding: utf-8 -*-
# @Time    : 2019/1/9
# @Author  : qirui
# @FileName: 752. Open the Lock.py


# 33 / 43 test cases passed. Status: Time Limit Exceeded
# class Solution(object):
#     def openLock(self, deadends, target):
#         """
#         :type deadends: List[str]
#         :type target: str
#         :rtype: int
#         """
#
#         if "0000" in deadends:
#             return -1
#
#         dict = {'0': ['9', '1'], '1': ['0', '2'], '2': ['1', '3'], '3': ['2', '4'], '4': ['3', '5'], '5': ['4', '6'],
#                 '6': ['5', '7'], '7': ['6', '8'], '8': ['7', '9'], '9': ['8', '0']}
#
#         queue, seen = ["0000"], set("0000")
#         level = 0
#
#         while queue:
#             level += 1
#             new_queue = []
#             for state in queue:
#                 for i, c in enumerate(state):
#                     for nei in dict[c]:
#                         next_state = state[:i] + nei + state[i + 1:]
#                         if next_state == target:
#                             return level
#                         if next_state in deadends or next_state in seen:
#                             continue
#                         seen.add(next_state)
#                         new_queue.append(next_state)
#             queue = new_queue
#
#         return -1

# BFS
class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """

        if "0000" in deadends:
            return -1

        dict = {'0': ['9', '1'], '1': ['0', '2'], '2': ['1', '3'], '3': ['2', '4'], '4': ['3', '5'], '5': ['4', '6'],
                '6': ['5', '7'], '7': ['6', '8'], '8': ['7', '9'], '9': ['8', '0']}

        queue, seen = ["0000"], set(deadends+["0000"])
        level = 0

        while queue:
            level += 1
            new_queue = []
            for state in queue:
                for i, c in enumerate(state):
                    for nei in dict[c]:
                        next_state = state[:i] + nei + state[i + 1:]
                        if next_state == target:
                            return level
                        if next_state not in seen:
                            seen.add(next_state)
                            new_queue.append(next_state)
            queue = new_queue

        return -1

# BFS
class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """

        if "0000" in deadends:
            return -1

        dict = {'0': ['9', '1'], '1': ['0', '2'], '2': ['1', '3'], '3': ['2', '4'], '4': ['3', '5'], '5': ['4', '6'],
                '6': ['5', '7'], '7': ['6', '8'], '8': ['7', '9'], '9': ['8', '0']}
        queue, seen = [("0000", 0)], set(deadends + ["0000"])

        while queue:
            state, level = queue.pop(0)
            for i, c in enumerate(state):
                for nei in dict[c]:
                    next_state = state[:i] + nei + state[i + 1:]
                    if next_state == target:
                        return level + 1
                    if next_state not in seen:
                        seen.add(next_state)
                        queue.append((next_state, level + 1))
        return -1


# BFS
class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """

        if "0000" in deadends:
            return -1

        queue, seen = [("0000", 0)], set(deadends + ["0000"])
        while queue:
            state, level = queue.pop(0)
            for i in range(4):
                for delta in [1, -1]:
                    next_state = state[:i] + str((int(state[i]) + delta) % 10) + state[i + 1:]
                    if next_state == target:
                        return level + 1
                    if next_state not in seen:
                        seen.add(next_state)
                        queue.append((next_state, level + 1))
        return -1

# BFS
class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """

        if "0000" in deadends:
            return -1

        queue, level, seen = ["0000"], 0, set(deadends + ["0000"])
        while queue:
            level += 1
            new_queue = []
            for state in queue:
                for i in range(4):
                    for delta in [1, -1]:
                        next_state = state[:i] + str((int(state[i]) + delta) % 10) + state[i + 1:]
                        if next_state == target:
                            return level
                        if next_state not in seen:
                            seen.add(next_state)
                            new_queue.append(next_state)
            queue = new_queue
        return -1


if __name__ == '__main__':
    S = Solution()
    deadends = ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"]
    target = "8888"
    print(S.openLock(deadends, target))
