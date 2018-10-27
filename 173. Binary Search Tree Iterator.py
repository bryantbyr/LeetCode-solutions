#173. Binary Search Tree Iterator

# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#Created by bryantbyr on 20181027
#Time:O(1)
#Space:O(N)
#Tree + Iteration
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.count = 0
        self.res = []
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                self.res.append(root.val)
                root = root.right

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.count < len(self.res):
            return True
        return False

    def next(self):
        """
        :rtype: int
        """
        res = self.res[self.count]
        self.count += 1
        return res

#Learn from discuss on 20181027
#Time:O(Log(N))
#Space:O(Log(N))
#Tree + Iteration
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0

    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        root = node.right
        while root:
            self.stack.append(root)
            root = root.left
        return node.val


# Your BSTIterator will be called like this:
t = TreeNode(2)
t.left = TreeNode(1)
# t.right = TreeNode(3)
# t.left.right = TreeNode(5)
# t.right.right = TreeNode(4)
i, v = BSTIterator(t), []
while i.hasNext(): v.append(i.next())
print(v)
