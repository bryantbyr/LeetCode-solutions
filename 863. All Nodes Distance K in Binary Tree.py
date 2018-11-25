# 863. All Nodes Distance K in Binary Tree

from tools import TreeNode, Tree
import collections

#Learn from discuss on 20181125
#Time:O(N^2)
#Space:O(N)
#Tree + DFS + BFS*
class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        conn = collections.defaultdict(set)

        def connect(root):
            if not root: return
            if root.left:
                conn[root.val].add(root.left.val)
                conn[root.left.val].add(root.val)
            if root.right:
                conn[root.val].add(root.right.val)
                conn[root.right.val].add(root.val)
            connect(root.left)
            connect(root.right)

        connect(root)
        res = [target.val]
        seen = set(res)
        for i in range(K):
            res = [y for x in res for y in conn[x] if y not in seen]
            seen |= set(res)
        return res


s = Solution()
T = Tree().creat_tree("1 null null")
print(s.distanceK(T, TreeNode(1), 3))
