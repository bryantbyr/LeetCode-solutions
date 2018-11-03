#508. Most Frequent Subtree Sum

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#Created by bryantbyr on 20181103
#Time:O(N)
#Space:O(N)
#Tree + Post Order Traversal
class Solution:
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        map1 = {}

        def helper(root):
            if not root: return 0
            cur_sum = helper(root.left) + helper(root.right) + root.val
            map1[cur_sum] = 1 if not map1.get(cur_sum) else map1[cur_sum] + 1
            return cur_sum

        helper(root)
        max_count, res = 0, []
        for key, value in map1.items():
            if value > max_count:
                max_count = value
                res.clear()
                res.append(key)
            elif value == max_count:
                res.append(key)
        return res

#Created by bryantbyr on 20181103
#Time:O(N)
#Space:O(N)
#Tree + Post Order Traversal
class Solution:
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        map1= {}

        def helper(root):
            if not root: return 0
            cur_sum = helper(root.left) + helper(root.right) + root.val
            map1[cur_sum] = 1 if not map1.get(cur_sum) else map1[cur_sum] + 1
            return cur_sum

        helper(root)
        res = []
        # for x in sorted(map1.items(), key=lambda map1: map1[1], reverse=True):
        #     if not res:
        #         res.append(x[0])
        #     elif x[1] == map1[res[0]]:
        #         res.append(x[0])
        #     else:
        #         break

        value_list = [v for v in sorted(map1.values())]
        if value_list:
            max_fre = value_list[-1]
            res = [k for k,v in map1.items() if v == max_fre]
        return res

#Created by bryantbyr on 20181103
#Time:O(N)
#Space:O(N)
#Tree + Post Order Traversal
class Solution:
    def __init__(self):
        self.max_count = 0

    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        map1 = {}

        def helper(root):
            if not root: return 0
            cur_sum = helper(root.left) + helper(root.right) + root.val
            map1[cur_sum] = 1 if not map1.get(cur_sum) else map1[cur_sum] + 1
            self.max_count = max(self.max_count, map1[cur_sum])
            return cur_sum

        helper(root)
        return [k for k, v in map1.items() if v == self.max_count]


s = Solution()
t = TreeNode(5)
t.left = TreeNode(2)
t.right = TreeNode(-5)
print(s.findFrequentTreeSum(t))
