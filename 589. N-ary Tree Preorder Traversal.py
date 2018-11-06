#589. N-ary Tree Preorder Traversal

# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

#Created by bryantbyr on 20181106
#Time:O(N)
#Space:O(N)
#Tree + Iteration
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res, stack = [], []
        while root or stack:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.children.pop(0) if root.children else None
            node = stack[-1]
            if node.children:
                root = node.children.pop(0)
            else:
                root = None
                stack.pop()
        return res


#Learn from discuss on 20181106
#Time:O(N)
#Space:O(N)
#Tree + Iteration/Stack
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root: return []
        res, stack = [], [root]
        while stack:
            root = stack.pop()
            res.append(root.val)
            stack.extend(root.children[::-1])
        return res


s = Solution()
t = Node(1, [Node(3, []), Node(2, []), Node(4, [])])
print(s.preorder(t))
