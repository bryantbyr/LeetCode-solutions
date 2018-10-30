#437. Path Sum III

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#Created by bryantbyr on 20181030
#Time:O(N^2)
#Space:O(N)
#Tree + Recursion
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """

        self.res = 0

        def helper(root, sum, temp):
            if not root: return
            temp += root.val
            if temp == sum:
                self.res += 1
            helper(root.left, sum, temp)
            helper(root.right, sum, temp)

        stack = []
        while root or stack:
            if root:
                helper(root, sum, 0)
                stack.append(root)
                root = root.left
            else:
                root = stack.pop().right
        return self.res

#Learn from discuss on 20181030
#Time:O(N^2)
#Space:O(1)
#Tree + Better Recursion
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """

        def helper(node, sum):
            if not node: return 0
            return (node.val == sum) + helper(node.left, sum - node.val) + helper(node.right, sum - node.val)

        if not root: return 0
        return helper(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)


S = Solution()
t = TreeNode(10)
t.left = TreeNode(5)
t.right = TreeNode(-3)
t.left.left = TreeNode(3)
t.left.right = TreeNode(2)
t.left.right.right = TreeNode(1)
t.left.left.left = TreeNode(3)
t.left.left.right = TreeNode(-2)
t.right.right = TreeNode(11)
print(S.pathSum(t, 8))
