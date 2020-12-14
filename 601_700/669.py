# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        def trim(node):
            if not node:
                return node
            if node.val < low:
                return trim(node.right)
            if node.val > high:
                return trim(node.left)
            node.left = trim(node.left)
            node.right = trim(node.right)
            return node

        return trim(root)
