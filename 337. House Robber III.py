#337. House Robber III

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#Learn from discuss on 20181030
#Time:O(N^2)
#Space:O(1)
#Tree + Recursion
Time Limit Exceeded
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        val = 0
        if root.left:
            val += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            val += self.rob(root.right.left) + self.rob(root.right.right)
        return max(root.val + val, self.rob(root.left) + self.rob(root.right))


#Learn from discuss on 20181030
#Time:O(N)
#Space:O(N)
#Tree + DP
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def helper(root, map):
            if not root: return 0
            if map.get(root): return map[root]
            val = 0
            if root.left:
                val += helper(root.left.left, map) + helper(root.left.right, map)
            if root.right:
                val += helper(root.right.left, map) + helper(root.right.right, map)
            val = max(root.val + val, helper(root.left, map) + helper(root.right, map))
            map[root] = val
            return val

        return helper(root, {})


#Learn from discuss on 20181031
#Time:O(N)
#Space:O(1)
#Tree + Greedy
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def helper(root):
            if not root: return (0, 0)
            left, right = helper(root.left), helper(root.right)
            return (max(left[0], left[1]) + max(right[0], right[1]), left[0] + right[0] + root.val)

        return max(helper(root))


s = Solution()
t = TreeNode(3)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.left.right = TreeNode(3)
t.right.right = TreeNode(1)
print(s.rob(t))
