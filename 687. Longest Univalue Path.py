# 687. Longest Univalue Path.py

from tools import TreeNode, Tree


# Time Limit Exceeded
# class Solution:
#     def __init__(self):
#         self.ans = 0
#
#     def longestUnivaluePath(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#
#         if not root: return 0
#         pre = root.val
#
#         def get_depth(node):
#             if not node or node.val != pre: return 0
#             return 1 + max(get_depth(node.left), get_depth(node.right))
#
#         def helper(node):
#             if not node or node.val != pre: return 0
#             return max(1 + get_depth(node.left) + get_depth(node.right), helper(node.left), helper(node.right))
#
#         cur = helper(root)
#         if cur > self.ans:
#             self.ans = cur
#         self.longestUnivaluePath(root.left)
#         self.longestUnivaluePath(root.right)
#
#         return self.ans - 1

#Learn from discuss on 20181113
#Time:O(N)
#Space:O(N)
#Tree + Recursion*
class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0

        def helper(node):
            if not node: return
            left_len, right_len = helper(node.left), helper(node.right)
            left = left_len + 1 if node.left and node.left.val == node.val else 0
            right = right_len + 1 if node.right and node.right.val == node.val else 0
            self.ans = max(self.ans, left + right)
            return max(left, right)

        helper(root)
        return self.ans


S = Solution()
T = Tree()
t = T.creat_tree("1 4 4 null null 4 null null 5 null 5 null null")
print(S.longestUnivaluePath(t))
