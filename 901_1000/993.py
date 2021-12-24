# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        x_depth = y_depth = x_parent = y_parent = 0

        def dfs(node, depth, parent):
            if not node:
                return
            if node.val == x:
                nonlocal x_depth, x_parent
                x_depth, x_parent = depth, parent
            if node.val == y:
                nonlocal y_depth, y_parent
                y_depth, y_parent = depth, parent
            dfs(node.left, depth + 1, node.val)
            dfs(node.right, depth + 1, node.val)

        dfs(root, 0, 0)
        return x_depth == y_depth and x_parent != y_parent
