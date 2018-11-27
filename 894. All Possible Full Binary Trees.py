# 894. All Possible Full Binary Trees


from tools import TreeNode, Tree

#Created by bryantbyr on 20181127
#Time:O(N^2)
#Space:O(1)
#Tree + Recursion
class Solution:
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """

        if N % 2 == 0: return []

        def helper(n):
            if n == 1:
                return [TreeNode(0)]
            i, res = 1, []
            while i < n - 1:
                left, right = helper(i), helper(n - 1 - i)
                for x in left:
                    for y in right:
                        root = TreeNode(0)
                        root.left = x
                        root.right = y
                        res.append(root)
                i += 2
            return res

        return helper(N)


S = Solution()
res = S.allPossibleFBT(5)
for x in res:
    Tree().front_recursion(x)
    print("----")
