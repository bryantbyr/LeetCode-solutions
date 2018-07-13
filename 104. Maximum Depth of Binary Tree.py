#104. Maximum Depth of Binary Tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#Created by bryantbyr on 20180713
#Space:O(1)
#Time:O(n)
#recursion
class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return max(self.maxDepth(root.left)+1,self.maxDepth(root.right)+1)


#Created by bryantbyr on 20180713
#Space:O(1)
#Time:O(n)
#no recursion
class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack, result = [], 0
        if root:
            stack.append(root)
        while stack:
            result += 1
            temp = []
            for x in stack:
                if x.left:
                    temp.append(x.left)
                if x.right:
                    temp.append(x.right)
            stack = temp[:]
        return result


s = Solution()
t1 = TreeNode(3)
t1.left = TreeNode(9)
t1.right = TreeNode(20)
t1.right.right = TreeNode(7)
t1.right.left = TreeNode(15)
print(s.maxDepth(t1))
