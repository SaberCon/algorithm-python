# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        def dfs(node, num):
            num += node.val
            if not node.left and not node.right:
                return num < limit
            if node.left and dfs(node.left, num):
                node.left = None
            if node.right and dfs(node.right, num):
                node.right = None
            return not node.left and not node.right

        return None if dfs(root, 0) else root
