import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#Learn from solution on 20181107
#Time:O(N^2)
#Space:O(N)
#Tree + serialize tree + Recursion
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """

        count, res = collections.Counter(), []

        def helper(root):
            if root == None: return "null"
            serial = str(root.val) + helper(root.left) + helper(root.right)
            count[serial] += 1
            if count[serial] == 2:
                res.append(root)
            return serial

        helper(root)
        return res


S = Solution()
t1 = TreeNode(1)
t1.left = TreeNode(2)
t1.left.left = TreeNode(4)
t1.right = TreeNode(3)
t1.right.right = TreeNode(4)
t1.right.left = TreeNode(2)
t1.right.left.left = TreeNode(4)
list = S.findDuplicateSubtrees(t1)
for x in list:
    print(x.val)
