# 99. Recover Binary Search Tree

from tools import Tree, TreeNode

#Learn from discuss on 20181204
#Time:O(N)
#Space:O(N)
#in_order_traversal recursively
class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        self.first, self.second, self.pre = None, None, None

        def in_order_traversal(root):
            if not root: return
            in_order_traversal(root.left)

            if self.pre:
                if root.val < self.pre.val and not self.first:
                    self.first = self.pre
                if root.val < self.pre.val and self.first:
                    self.second = root

            self.pre = root
            in_order_traversal(root.right)

        in_order_traversal(root)
        temp = self.second.val
        self.second.val = self.first.val
        self.first.val = temp

#Learn from discuss on 20181206
#Time:O(N)
#Space:O(1)
#in_order_traversal using Morris Traversal
class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        self.first, self.second, self.pre = None, None, None

        def in_order_traversal(root):
            current = root

            while current:
                if not current.left:
                    if self.pre:
                        if current.val < self.pre.val:
                            if not self.first:
                                self.first = self.pre
                            if self.first:
                                self.second = current
                    self.pre = current
                    current = current.right
                else:
                    pre = current.left
                    while pre.right and pre.right != current:
                        pre = pre.right

                    if not pre.right:
                        pre.right = current
                        current = current.left
                    else:
                        if self.pre:
                            if current.val < self.pre.val:
                                if not self.first:
                                    self.first = self.pre
                                if self.first:
                                    self.second = current
                        self.pre = current
                        pre.right = None
                        current = current.right

        in_order_traversal(root)
        temp = self.second.val
        self.second.val = self.first.val
        self.first.val = temp


S = Solution()
T = Tree().creat_tree("3 1 null null 4 2 null null null")
S.recoverTree(T)
# Tree().front_recursion(T)
Tree().inOrder_MorrisTraversal(T)
