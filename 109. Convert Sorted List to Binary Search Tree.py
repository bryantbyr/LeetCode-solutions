# 109. Convert Sorted List to Binary Search Tree


from tools import Tree, TreeNode


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Learn from Solution on 20181208
# Time:O(N*Log(N))
# Space:O(Log(N))
# Two Pointers + List + BST
class Solution:

    def find_mid_node(self, head):
        pre = None
        fast, slow = head, head
        while fast and fast.next:
            pre = slow
            fast = fast.next.next
            slow = slow.next

        if pre:
            pre.next = None

        return slow

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        if not head: return None
        if not head.next: return TreeNode(head.val)

        slow = self.find_mid_node(head)
        root = TreeNode(slow.val)
        root.left, root.right = self.sortedListToBST(head), self.sortedListToBST(slow.next)
        return root

# Created by bryantbyr on 20181208
# Time:O(N*Log(N))
# Space:O(N)
# List + BST
class Solution:

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        vals = []

        def listNode_to_list(head):
            while head:
                vals.append(head.val)
                head = head.next

        listNode_to_list(head)

        def helper(list):
            if not list: return None
            mid = len(list)//2
            root = TreeNode(list[mid])
            root.left, root.right = helper(list[:mid]), helper(list[mid+1:])
            return root

        return helper(vals)

# Created by bryantbyr on 20181208
# Time:O(N)
# Space:O(N)
# List + BST
class Solution:

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        vals = []

        def listNode_to_list(head):
            while head:
                vals.append(head.val)
                head = head.next

        listNode_to_list(head)

        def helper(l, r):
            if l > r: return None
            mid = (l + r) // 2
            root = TreeNode(vals[mid])
            root.left, root.right = helper(l, mid - 1), helper(mid + 1, r)
            return root

        return helper(0, len(vals) - 1)

# Learn from Solution on 20181208
# Time:O(N)
# Space:O(Log(N))
# Two Pointers + List + BST
class Solution:

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        # length = 0
        #
        # def find_size(head):
        #     nonlocal length
        #     while head:
        #         length += 1
        #         head = head.next
        #
        # find_size(head)


        def find_size(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length

        length = find_size(head)

        def helper(l, r):
            nonlocal head  # 将head声明为外层变量

            if l > r: return None
            mid = (l + r) // 2
            left = helper(l, mid - 1)

            root = TreeNode(head.val)
            root.left = left

            head = head.next
            root.right = helper(mid + 1, r)
            return root

        return helper(0, length - 1)


if __name__ == '__main__':
    S = Solution()
    L = ListNode(-10)
    L.next = ListNode(3)
    L.next.next = ListNode(0)
    L.next.next.next = ListNode(5)
    L.next.next.next.next = ListNode(9)
    Tree().front_recursion(S.sortedListToBST(L))
