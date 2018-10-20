#102. Binary Tree Level Order Traversal

import queue
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#Created by bryantbyr on 20181020
#Time:O(N)
#Space:O(N)
#Tree + Queue
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        q1 = queue.Queue()
        q1.put(root)
        while not q1.empty():
            level = []
            q2 = queue.Queue()
            while not q1.empty():
                node = q1.get()
                level.append(node.val)
                if node.left:
                    q2.put(node.left)
                if node.right:
                    q2.put(node.right)
            res.append(level)
            q1 = q2
        return res

#Learn from discuss on 20181020
#Time:O(N)
#Space:O(N)
#Tree
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res, level = [], [root]
        while level:
            res.append([node.val for node in level])
            temp = []
            for node in level:
                temp.extend([node.left,node.right])
            level = [leaf for leaf in temp if leaf]
        return res

#Learn from discuss on 20181020
#Time:O(N)
#Space:O(N)
#Tree (pythonic)
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res, level = [], [root]
        while root and level:
            res.append([node.val for node in level])
            level = [kid for n in level for kid in (n.left,n.right) if kid]
        return res

s = Solution()
t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(7)
t.left.left = TreeNode(5)
# t.right.left = TreeNode(6)
t.right.right = TreeNode(8)
print(s.levelOrder(t))
