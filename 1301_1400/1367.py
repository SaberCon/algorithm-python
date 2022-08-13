# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if not head:
            return True
        if not root:
            return False
        return self.isSubPathFromRoot(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    def isSubPathFromRoot(self, head: ListNode, root: TreeNode) -> bool:
        if not head:
            return True
        if not root:
            return False
        return head.val == root.val and \
            (self.isSubPathFromRoot(head.next, root.left) or self.isSubPathFromRoot(head.next, root.right))
