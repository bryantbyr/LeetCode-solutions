#637. Average of Levels in Binary Tree
#
#Created by bryantbyr on 20180713
#Space:O(n)
#Time:O(n)
#二叉树的层次遍历

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        r, level = [], [root]
        while level:
            lenOfEachLevel = len(level)
            total = lenOfEachLevel
            temp = 0
            while lenOfEachLevel != 0:
                node = level.pop(0)
                temp += node.val
                if node.left is not None:
                    level.append(node.left)
                if node.right is not None:
                    level.append(node.right)
                lenOfEachLevel -= 1
            r.append(temp / total)
        return r

        # def averageOfLevels(self, root):
        #     """
        #     :type root: TreeNode
        #     :rtype: List[float]
        #     """
        #     if not root:
        #         return []
        #     result, stack = [], [root]
        #     while stack:
        #         temp, sums = [], 0
        #         for item in stack:
        #             sums += item.val
        #             if item.left:
        #                 temp.append(item.left)
        #             if item.right:
        #                 temp.append(item.right)
        #         result.append(sums / len(stack))
        #         stack = temp[:]
        #     return result


s = Solution()
t1 = TreeNode(3)
t1.left = TreeNode(9)
t1.right = TreeNode(20)
t1.right.right = TreeNode(7)
t1.right.left = TreeNode(15)
list = s.averageOfLevels(t1)
for x in list:
    print(x)
