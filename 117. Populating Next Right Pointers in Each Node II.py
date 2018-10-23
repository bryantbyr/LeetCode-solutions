#117. Populating Next Right Pointers in Each Node II

# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

#Learn from discuss on 20181023
#Time:O(N)
#Space:O(1)
#Tree + Iteration
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        tail = dummy = TreeLinkNode(0)
        while root:
            tail.next = root.left
            if tail.next:
                tail = tail.next
            tail.next = root.right
            if tail.next:
                tail = tail.next
            root = root.next
            if not root:
                tail, root = dummy, dummy.next
