#662. Maximum Width of Binary Tree

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Time Limit Exceeded
# class Solution:
#     def widthOfBinaryTree(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         if not root: return 0
#         level, ans, count = [root], 1, 1
#         while any(level):
#             temp, count, right_count, left_count = [], count * 2, 0, 0
#             for node in level:
#                 if node:
#                     temp.append(node.left)
#                     right_count = 0 if node.left else right_count + 1
#                     if not any(temp):
#                         left_count = right_count
#                     temp.append(node.right)
#                     right_count = 0 if node.right else right_count + 1
#                 else:
#                     temp.extend([None, None])
#                     right_count += 2
#                 if not any(temp):
#                     left_count = right_count
#             level, ans = temp, max(ans, count - right_count - left_count)
#         return ans

#Learn from discuss on 20181109
#Time:O(N)
#Space:O(N)
#Tree + BFS
class Solution:
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [(root, 0, 0)]
        cur_depth = left = ans = 0
        for node, depth, pos in queue:
            if node:
                queue.append((root.left, depth + 1, pos * 2))
                queue.append((root.right, depth + 1, pos * 2 + 1))
                if cur_depth != depth:
                    cur_depth = depth
                    left = pos
                ans = max(pos - left + 1, ans)
        return ans


s = Solution()
t = TreeNode(5)
t.left = TreeNode(3)
t.right = TreeNode(6)
# t.left.right = TreeNode(4)
t.left.left = TreeNode(2)
t.right.left = TreeNode(7)
print(s.widthOfBinaryTree(t))
