# 919. Complete Binary Tree Inserter


from tools import TreeNode, Tree
import collections

#Created by bryantbyr on 20181201
#Time:O(N)
#Space:O(1)
#Tree + BFS + OOD
class CBTInserter:

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.deque = collections.deque()
        q = [root]
        while q:
            node = q.pop(0)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            if not node.left or not node.right:
                self.deque.append(node)

    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        parent = self.deque[0]
        if not parent.left:
            parent.left = TreeNode(v)
        else:
            parent.right = TreeNode(v)
            self.deque.popleft()
        self.deque.append(TreeNode(v))
        return parent.val

    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.root


T = Tree().creat_tree("1 2 3 null null null 4 null null")
obj = CBTInserter(T)
print(obj.insert(7))
