# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        def unival(node, val):
            if not node:
                return True
            if node.val != val:
                return False
            return unival(node.left, val) and unival(node.right, val)

        return unival(root, root.val)
