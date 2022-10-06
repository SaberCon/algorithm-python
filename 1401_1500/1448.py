# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, num: int) -> int:
            if not node:
                return 0
            return (node.val >= num) + dfs(node.left, max(node.val, num)) + dfs(node.right, max(node.val, num))

        return dfs(root, -10000)
