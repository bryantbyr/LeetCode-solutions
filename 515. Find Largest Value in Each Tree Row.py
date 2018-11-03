#515. Find Largest Value in Each Tree Row

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#Created by bryantbyr on 20181103
#Time:O(N)
#Space:O(N)
#Tree + Level Traversal/BFS
class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        level, res = [root], []
        while level:
            temp, Max = [], 0
            for i in range(len(level)):
                Max = level[i].val if i == 0 else max(Max, level[i].val)
                if level[i].left:
                    temp.append(level[i].left)
                if level[i].right:
                    temp.append(level[i].right)
            level = temp
            res.append(Max)
        return res

#Created by bryantbyr on 20181103
#Time:O(N)
#Space:O(N)
#Tree + Level Traversal/BFS
class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        level, res = [root], [root.val]
        while level:
            temp, Max = [], 0
            for node in level:
                for kid in (node.left, node.right):
                    if kid:
                        Max = kid.val if not temp else max(Max, kid.val)
                        temp.append(kid)
            level = temp
            if level:
                res.append(Max)
        return res

#Created by bryantbyr on 20181103
#Time:O(N^2)
#Space:O(N)
#Tree + Level Traversal/BFS
class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        level, res = [root], []
        while level:
            res.append(max(node.val for node in level))
            level = [kid for node in level for kid in (node.left, node.right) if kid]
        return res


s = Solution()
t = TreeNode(5)
t.left = TreeNode(2)
t.right = TreeNode(-5)
print(s.largestValues(t))
