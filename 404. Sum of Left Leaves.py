#404. Sum of Left Leaves

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#Created by bryantbyr on 20180806
#Time:O(N)
#Space:O(1)
#recusion traverse
class Solution:
    def __init__(self):
        self.val = 0
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return self.val
        if root.left and not root.left.left and not root.left.right:
            self.val += root.left.val
        self.sumOfLeftLeaves(root.left)
        self.sumOfLeftLeaves(root.right)
        return self.val


#Learn from discuss on 20180806
#Time:O(N)
#Space:O(1)
#recusion traverse(looks better)
class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if root.left and not root.left.left and not root.left.right:
            left = root.left.val
        else:
            left = self.sumOfLeftLeaves(root.left)
        right = self.sumOfLeftLeaves(root.right)
        return left + right


s = Solution()
t1 = TreeNode(3)
t1.left = TreeNode(9)
t1.left.right = TreeNode(1)
t1.left.left = TreeNode(10)
t1.right = TreeNode(20)
t1.right.left = TreeNode(15)
t1.right.right = TreeNode(7)
print(s.sumOfLeftLeaves(t1))
