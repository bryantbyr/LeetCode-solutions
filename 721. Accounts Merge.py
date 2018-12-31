# -*- coding: utf-8 -*-
# @Time    : 2018/12/31
# @Author  : qirui
# @FileName: 721. Accounts Merge.py

import collections


# Time:O(N)
# Space:O(N)
# DFS to find all connected components of graph
class Solution:
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """

        graph, email_to_name = collections.defaultdict(set), {}
        for acc in accounts:
            for email in acc[1:]:
                graph[acc[1]].add(email)
                graph[email].add(acc[1])
                email_to_name[email] = acc[0]

        def dfs(v):
            seen.add(v)
            temp.append(v)
            for nei in graph[v]:
                if nei not in seen:
                    dfs(nei)

        res, seen = [], set()
        for node in graph:
            if node not in seen:
                temp = list()
                dfs(node)
                res.append([email_to_name[node]] + sorted(temp))
        return res

# Time:O(N)
# Space:O(N)
# BFS to find all connected components of graph
class Solution:
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """

        graph, email_to_name = collections.defaultdict(set), {}
        for acc in accounts:
            for email in acc[1:]:
                graph[acc[1]].add(email)
                graph[email].add(acc[1])
                email_to_name[email] = acc[0]

        res, seen = [], set()
        for node in graph:
            if node not in seen:
                seen.add(node)
                queue = [node]
                temp = list()
                while queue:
                    cur = queue.pop(0)
                    temp.append(cur)
                    for nei in graph[cur]:
                        if nei not in seen:
                            seen.add(nei)
                            queue.append(nei)
                res.append([email_to_name[node]] + sorted(temp))
        return res

# Time:O(N)
# Space:O(N)
# DFS in iteration find all connected components of graph
class Solution:
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """

        graph, email_to_name = collections.defaultdict(set), {}
        for acc in accounts:
            for email in acc[1:]:
                graph[acc[1]].add(email)
                graph[email].add(acc[1])
                email_to_name[email] = acc[0]

        res, seen = [], set()
        for node in graph:
            if node not in seen:
                seen.add(node)
                stack = [node]
                temp = list()
                while stack:
                    cur = stack.pop()
                    temp.append(cur)
                    for nei in graph[cur]:
                        if nei not in seen:
                            seen.add(nei)
                            stack.append(nei)
                res.append([email_to_name[node]] + sorted(temp))
        return res


if __name__ == '__main__':
    S = Solution()
    accounts = [["Alex", "Alex5@m.co", "Alex4@m.co", "Alex0@m.co"],
                ["Ethan", "Ethan3@m.co", "Ethan3@m.co", "Ethan0@m.co"],
                ["Kevin", "Kevin4@m.co", "Kevin2@m.co", "Kevin2@m.co"],
                ["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe2@m.co"], ["Gabe", "Gabe3@m.co", "Gabe4@m.co", "Gabe2@m.co"]]
    print(S.accountsMerge(accounts))
