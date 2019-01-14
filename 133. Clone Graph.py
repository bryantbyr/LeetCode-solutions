# -*- coding: utf-8 -*-
# @Time    : 2019/1/14
# @Author  : qirui
# @FileName: 133. Clone Graph.py


# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


# Time: O(N)
# Space: O(N)
# BFS
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):

        if not node:
            return None

        new_node = UndirectedGraphNode(node.label)
        queue_1, queue_2, dict = [node], [new_node], {node: new_node}

        while queue_1:
            cur = queue_1.pop(0)
            tmp = queue_2.pop(0)
            for nei in cur.neighbors:
                if nei not in dict:
                    new_nei = UndirectedGraphNode(nei.label)
                    tmp.neighbors.append(new_nei)
                    dict[nei] = new_nei
                    queue_1.append(nei)
                    queue_2.append(new_nei)
                else:
                    tmp.neighbors.append(dict[nei])

        return new_node


# Time: O(N)
# Space: O(N)
# DFS
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):

        if not node:
            return None

        def dfs(v, new_v):
            for nei in v.neighbors:
                if nei not in dict:
                    new_nei = UndirectedGraphNode(nei.label)
                    dict[nei] = new_nei
                    dfs(nei, new_nei)
                new_v.neighbors.append(dict[nei])

        new_node = UndirectedGraphNode(node.label)
        dict = {node: new_node}
        dfs(node, new_node)
        return new_node

# Learn from discuss
# Time: O(N)
# Space: O(N)
# BFS optimization
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):

        if not node:
            return None

        new_node = UndirectedGraphNode(node.label)
        queue, dict = [node], {node: new_node}

        while queue:
            cur = queue.pop(0)
            for nei in cur.neighbors:
                if nei not in dict:
                    dict[nei] = UndirectedGraphNode(nei.label)
                    queue.append(nei)
                dict[cur].neighbors.append(dict[nei])

        return new_node

# Learn from discuss
# Time: O(N)
# Space: O(N)
# DFS iteratively
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):

        if not node:
            return None

        new_node = UndirectedGraphNode(node.label)
        queue, dict = [node], {node: new_node}

        while queue:
            cur = queue.pop()
            for nei in cur.neighbors:
                if nei not in dict:
                    dict[nei] = UndirectedGraphNode(nei.label)
                    queue.append(nei)
                dict[cur].neighbors.append(dict[nei])

        return new_node


# Time: O(N)
# Space: O(N)
# DFS with optimization
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):

        if not node:
            return None

        def dfs(v):
            for nei in v.neighbors:
                if nei not in dict:
                    dict[nei] = UndirectedGraphNode(nei.label)
                    dfs(nei)
                dict[v].neighbors.append(dict[nei])

        new_node = UndirectedGraphNode(node.label)
        dict = {node: new_node}
        dfs(node)
        return new_node


if __name__ == '__main__':
    S = Solution()
    node = UndirectedGraphNode(0)
    node.neighbors = [UndirectedGraphNode(0), UndirectedGraphNode(0)]
    print(S.cloneGraph(node).neighbors)
