#501. Find Mode in Binary Search Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#Created by bryantbyr on 20181102
#Time:O(N)
#Space:O(1)
#Tree + in_order_traversal/Recursion
class Solution:
    def __init__(self):
        self.max_count = 0
        self.cur_count = 0
        self.pre = 0

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        res, self.pre = [], root.val

        def in_order_traversal(root):
            if not root: return
            in_order_traversal(root.left)
            if root.val == self.pre:
                self.cur_count += 1
            else:
                self.cur_count = 1
                self.pre = root.val
            if self.cur_count > self.max_count:
                self.max_count = self.cur_count
                res.clear()
                res.append(root.val)
            elif self.cur_count == self.max_count:
                res.append(root.val)
            in_order_traversal(root.right)

        in_order_traversal(root)
        return res


#Created by bryantbyr on 20181102
#Time:O(N)
#Space:O(N)
#Tree + in_order_traversal
class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if not root: return []

        max_count, cur_count, pre = 0, 0, root.val
        res, stack = [], []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()

            cur_count = cur_count + 1 if root.val == pre else 1
            pre = root.val
            # if root.val == pre:
            #     cur_count += 1
            # else:
            #     cur_count = 1
            #     pre = root.val
            #
            if cur_count > max_count:
                max_count = cur_count
                res.clear()
                res.append(root.val)
            elif cur_count == max_count:
                res.append(root.val)
            root = root.right

        return res


s = Solution()
t1 = TreeNode(1)
t1.right = TreeNode(2)
t1.right.right = TreeNode(2)
print(s.findMode(t1))
