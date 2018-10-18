#95. Unique Binary Search Trees II

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#Learn from solution on 20181018
#Time:O(n^2)
#Space:O(n)
#Tree + DP
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


s = Solution()
for x in s.generateTrees(3):
    print(x.val)
