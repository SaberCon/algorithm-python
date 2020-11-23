class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        max_level = 0
        leftmost = 0

        def dfs(node, level):
            if not node:
                return
            nonlocal max_level, leftmost
            if level > max_level:
                max_level = level
                leftmost = node.val
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 1)
        return leftmost
