#230. Kth Smallest Element in a BST

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#Created by bryanybyr on 20181026
#Time:O(N)
#Space:O(1)
#Tree + Iteration
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                k -= 1
                if k == 0:
                    return root.val
                root = root.right

#Created by bryanybyr on 20181026
#Time:O(N)
#Space:O(1)
#Tree + Iteration
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right

#Learn from discuss on 20181027
#Time:O(N*Log(N))
#Space:O(1)
#Tree + Binary Search
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        def count(node):
            if not node:
                return 0
            return 1 + count(node.left) + count(node.right)

        count = count(root.left)
        if count >= k:
            return self.kthSmallest(root.left, k)
        elif count < k - 1:
            return self.kthSmallest(root.right, k - count - 1)
        return root.val


s = Solution()
t = TreeNode(3)
t.left = TreeNode(1)
t.right = TreeNode(4)
# t.left.left = TreeNode(0)
t.left.right = TreeNode(2)
# t.left.right.left = TreeNode(3)
# t.left.right.right = TreeNode(5)
# t.right.right = TreeNode(9)
# t.right.left = TreeNode(7)
print(s.kthSmallest(t, 1))
