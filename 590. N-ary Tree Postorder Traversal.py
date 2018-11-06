#590. N-ary Tree Postorder Traversal

# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

#Learn from discuss on 20181106
#Time:O(N)
#Space:O(N)
#Tree + Iteration/Stack*
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root: return
        res, stack = [], [root]
        while stack:
            root = stack.pop()
            res.append(root.val)
            if root.children:
                stack.extend(root.children)
        return res[::-1]


s = Solution()
t = Node(1, [Node(3, []), Node(2, []), Node(4, [])])
print(s.postorder(t))
