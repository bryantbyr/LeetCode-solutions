#199. Binary Tree Right Side View

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#Learn from discuss on 20181027
#Time:O(N)
#Space:O(1)
#Tree + Preorder Traversal
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def helper(root, res, k):
            if not root: return
            if res.__len__() == k:
                res.append(root.val)
            helper(root.right, res, k + 1)
            helper(root.left, res, k + 1)

        res = []
        helper(root, res, 0)
        return res

#Learn from discuss on 20181027
#Time:O(N)
#Space:O(N)
#Tree + Level Traversal
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return
        res, queue = [], [root]
        while queue:
            length = len(queue)
            for i in range(length):
                node = queue.pop(0)
                if i == length - 1:
                    res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res


s = Solution()
t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.left.right = TreeNode(5)
t.right.right = TreeNode(4)
print(s.rightSideView(t))
