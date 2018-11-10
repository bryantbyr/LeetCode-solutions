# 449. Serialize and Deserialize BST

import collections


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#Learn from discuss on 20181110
#Time:O(N)
#Space:O(N)
#Tree + Recursion + BST
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        vals = []

        def preOrder(node):
            if node:
                vals.append(node.val)
                preOrder(node.left)
                preOrder(node.right)

        preOrder(root)
        return ' '.join(map(str, vals))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        vals = collections.deque(int(val) for val in data.split())

        def build(minVal, maxVal):
            if vals and minVal < vals[0] < maxVal:
                val = vals.popleft()
                node = TreeNode(val)
                node.left = build(minVal, val)
                node.right = build(val, maxVal)
                return node

        return build(float('-inf'), float('inf'))


# Your Codec object will be instantiated and called as such:
codec = Codec()
t = TreeNode(5)
t.left = TreeNode(2)
t.left.right = TreeNode(4)
t.right = TreeNode(9)
codec.deserialize(codec.serialize(t))
