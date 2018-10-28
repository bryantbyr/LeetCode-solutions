#236. Lowest Common Ancestor of a Binary Tree

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#Created by bryantbyr on 20181028
#Time:O(N*Log(N))
#Space:O(N)
#Tree + Iteration + Traversal
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        def inorder_traversal(root, res):
            stack = []
            while stack or root:
                while root:
                    stack.append(root)
                    root = root.left
                root = stack.pop()
                res.append(root)
                root = root.right

        res = []
        inorder_traversal(root, res)
        p_index, q_index,root_index = res.index(p), res.index(q),res.index(root)
        while (root_index - p_index) * (root_index - q_index) > 0:
            root = root.left if (root_index - p_index) > 0 else root.right
            root_index = res.index(root)
        return root


# Time Limit Exceeded
# class Solution(object):
#     def lowestCommonAncestor(self, root, p, q):
#         """
#         :type root: TreeNode
#         :type p: TreeNode
#         :type q: TreeNode
#         :rtype: TreeNode
#         """
#
#         def inorder_traversal(root, p, q):
#             isP, isQ, stack = False, False, []
#             while stack or root:
#                 while root:
#                     stack.append(root)
#                     root = root.left
#                 root = stack.pop()
#                 if p == root: isP = True
#                 if q == root: isQ = True
#                 if isP and isQ: return True
#                 root = root.right
#             return False
#
#         left, right = inorder_traversal(root.left, p, q), inorder_traversal(root.right, p, q)
#         while left or right:
#             root = root.left if left else root.right
#             left, right = inorder_traversal(root.left, p, q), inorder_traversal(root.right, p, q)
#         return root

#Learn from discuss on 20181028
#Time:O(N)
#Space:O(1)
#Tree + Recursion
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root in (None, p, q): return root
        left, right = self.lowestCommonAncestor(root.left, p, q), self.lowestCommonAncestor(root.right, p, q)
        if not left:
            return right
        elif not right:
            return left
        return root


s = Solution()
t = TreeNode(3)
t.left = TreeNode(5)
t.right = TreeNode(1)
t.left.left = TreeNode(0)
t.left.right = TreeNode(4)
t.left.right.left = TreeNode(3)
t.left.right.right = TreeNode(5)
t.right.right = TreeNode(9)
t.right.left = TreeNode(7)
print(s.lowestCommonAncestor(t, t.left, t.right).val)
