# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right) \
               + (root.left is not None and root.left.left is None and root.left.right is None and root.left.val)
