#95. Unique Binary Search Trees II

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#Learn from solution on 20181018
#Time:O(2^N)
#Space:O(n)
#Tree + Recursion
class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n==0:
            return []
        return self.cal([i for i in range(1, n + 1)])

    def cal(self, lst):
        if not lst:
            return [None]
        res = []
        for i in range(len(lst)):
            for left in self.cal(lst[:i]):
                for right in self.cal(lst[i + 1:]):
                    node, node.left, node.right = TreeNode(lst[i]), left, right
                    res += [node]
        return res

#Learn from solution on 20181019
#Time:O(2^N)
#Space:O(N^2)
#Tree + DP
class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        dp = [[] for i in range(0, n + 1)]
        dp[0].append(None)
        for i in range(1, n + 1):
            for j in range(0, i):
                for left in dp[j]:
                    for right in dp[i - (j + 1)]:
                        node = TreeNode(j + 1)
                        node.left = left
                        node.right = self.clone(right, j + 1)
                        dp[i].append(node)
        return dp[n]

    def clone(self, node, offset):
        if not node:
            return None
        newNode = TreeNode(node.val + offset)
        newNode.right = self.clone(node.right, offset)
        newNode.left = self.clone(node.left, offset)
        return newNode


s = Solution()
r = s.generateTrees(3)
print(r)
for x in r:
    if x:
        print(x.val)
