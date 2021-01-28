# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def prune(node):
            if not node:
                return None
            node.left, node.right = prune(node.left), prune(node.right)
            if not (node.val and node.left and node.right):
                return None
            return node

        return prune(root)
