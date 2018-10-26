#145. Binary Tree Postorder Traversal

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#Created by bryantbyr on 20181026
#Time:O(N)
#Space:O(N)
#Tree + Iteration
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack, res, node, lastNode = [root], [], root, None
        while node and stack:
            while node.left:
                stack.append(node.left)
                node = node.left
            root = stack.pop()
            if not root.right or lastNode == root.right:
                res.append(root.val)
                lastNode = root
            else:
                stack.append(root)
                node = root.right
                stack.append(node)
        return res

#Learn from discuss on 20181026
#Time:O(N)
#Space:O(N)
#Tree + Clever Iteration
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack, res = [], []
        while root or stack:
            while root:
                res.insert(0, root.val)
                stack.append(root)
                root = root.right
            root = stack.pop().left
        return res


s = Solution()
t = TreeNode(4)
t.left = TreeNode(9)
t.right = TreeNode(0)
t.left.left = TreeNode(5)
t.left.right = TreeNode(1)
t.right.right = TreeNode(4)
t.right.right.right = TreeNode(1)
t.right.left = TreeNode(13)
print(s.postorderTraversal(t))
