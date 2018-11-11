# 297. Serialize and Deserialize Binary Tree

import collections
from tools import Tree, TreeNode

#Created by bryantbyr on 20181111
#Time:O(N)
#Space:O(N)
#Tree + Recursion
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        vals = []

        def pre_order(node):
            if node:
                vals.append(str(node.val))
                pre_order(node.left)
                pre_order(node.right)
            else:
                vals.append('null')

        pre_order(root)
        return ' '.join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        vals = collections.deque(data.split())

        def build_tree():
            val = vals.popleft()
            if val != 'null':
                node = TreeNode(int(val))
                node.left = build_tree()
                node.right = build_tree()
                return node
            else:
                return None

        return build_tree()


# Your Codec object will be instantiated and called as such:
codec = Codec()
t = TreeNode(5)
t.left = TreeNode(2)
t.left.right = TreeNode(4)
t.right = TreeNode(9)
root = codec.deserialize(codec.serialize(t))
Tree().front_recursion(root)
