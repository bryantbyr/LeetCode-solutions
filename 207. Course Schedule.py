# 207. Course Schedule

import collections

# Learn from Solution on 20181217
# Time:O(V+E)
# Space:O(V+E)
# DFS + Graph
class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        def make_graph(adjEdges):
            for u, v in adjEdges:
                graph[v].append(u)

        def isCyclicUtil(v, visited, resStack):
            visited[v] = True
            resStack[v] = True
            for neighbor in graph[v]:
                # if not visited[neighbor] and isCyclicUtil(neighbor, visited, resStack):
                #     return True
                # elif resStack[neighbor]:
                #     return True

                # if (visited[neighbor] and resStack[neighbor]) or (not visited[neighbor] and isCyclicUtil(neighbor, visited, resStack)):
                #     return True

                if (not visited[neighbor] and isCyclicUtil(neighbor, visited, resStack)) or (resStack[neighbor]):
                    return True

            resStack[v] = False
            return False

        graph = collections.defaultdict(list)
        make_graph(prerequisites)
        visited = [False] * numCourses
        resStack = [False] * numCourses
        for node in range(numCourses):
            if not visited[node]:
                if isCyclicUtil(node, visited, resStack):
                    return False
        return True


if __name__ == '__main__':
    S = Solution()
    print(S.canFinish(2, [[1, 0]]))
