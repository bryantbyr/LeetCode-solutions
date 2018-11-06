#623. Add One Row to Tree

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree(object):
    def front_recursion(self, root):
        """利用递归实现树的先序遍历"""
        if root is None:
            return
        print(root.val)
        self.front_recursion(root.left)
        self.front_recursion(root.right)


#Created by bryantbyr on 20181106
#Time:O(N)
#Space:O(N)
#Tree + Level Traversal
class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node
        level = [root]
        while d > 2:
            level, d = [kid for node in level for kid in (node.left, node.right) if kid], d - 1
        for node in level:
            v_left, v_left.left = TreeNode(v), node.left
            v_right, v_right.right = TreeNode(v), node.right
            node.left, node.right = v_left, v_right
        return root


s = Solution()
t = TreeNode(1)
t.left = TreeNode(3)
t.right = TreeNode(2)
t.left.left = TreeNode(5)

r = s.addOneRow(t, 4, 2)
Tree().front_recursion(r)
