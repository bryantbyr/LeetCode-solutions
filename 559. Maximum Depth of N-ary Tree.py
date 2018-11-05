#559. Maximum Depth of N-ary Tree

# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

#Created by bryanybyr on 20181105
#Time:O(N)
#Space:O(N)
#Tree + Recursion
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root: return 0
        temp = [self.maxDepth(kid) for kid in root.children]
        return max(temp) + 1 if temp else 1

#Created by bryanybyr on 20181105
#Time:O(N)
#Space:O(1)
#Tree + Recursion
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root: return 0
        if not root.children: return 1
        return max(self.maxDepth(kid) for kid in root.children) + 1


s = Solution()
t = Node(1, [Node(3, []), Node(2, []), Node(4, [])])
print(s.maxDepth(t))
