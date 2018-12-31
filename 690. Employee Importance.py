# -*- coding: utf-8 -*-
# @Time    : 2018/12/24
# @Author  : qirui
# @FileName: 690. Employee Importance.py


# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

# Time: O(N)
# Space: O(N)
# DFS
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """

        # dict = {}
        # for e in employees:
        #     dict[e.id] = (e.importance, e.subordinates)

        dict = {e.id: (e.importance, e.subordinates) for e in employees}

        def dfs(node):
            return dict[node][0] + sum([dfs(sub) for sub in dict[node][1]])

        return dfs(id)

# Time: O(N)
# Space: O(N)
# BFS
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """

        dict, queue, ans = {e.id: (e.importance, e.subordinates) for e in employees}, [id], 0
        while queue:
            cur = dict[queue.pop(0)]
            ans += cur[0]
            queue.extend(cur[1])
        return ans


if __name__ == '__main__':
    S = Solution()
    print(S.getImportance([Employee(1, 5, [2]), Employee(2, 3, [3]), Employee(3, 3, [])], 1))
