#684. Redundant Connection

import collections


#Learn from solution on 20181115
#Time:O(N^2)
#Space:O(N)
#Tree + DFS
class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = collections.defaultdict(set)

        def dfs(source,target):
            if source not in seen:
                if source==target: return True
                seen.add(source)
                return any(dfs(nei,target) for nei in graph[source])


        for u,v in edges:
            seen = set()
            if u in graph and v in graph and dfs(u,v):
                return u,v
            graph[u].add(v)
            graph[v].add(u)




S = Solution()
list = [[1,2], [2,3], [3,4], [1,4], [1,5]]
print(S.findRedundantConnection(list))
