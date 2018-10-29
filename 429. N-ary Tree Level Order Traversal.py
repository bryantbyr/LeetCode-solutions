#429. N-ary Tree Level Order Traversal

# definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

#Learn from discuss in 20181029
#Time:O(N)
#Space:O(1)
#Tree + Iteration(pythonic)
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root: return
        level, res = [root], []
        while level:
            res.append([x.val for x in level])
            level = [kid for node in level for kid in node.children if kid]
        return res
