# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        depth = ans = 0

        def dfs(node: TreeNode, d: int):
            nonlocal depth, ans
            if not node:
                return
            if d == depth:
                ans += node.val
            if d > depth:
                depth, ans = d, node.val
            dfs(node.left, d + 1)
            dfs(node.right, d + 1)

        dfs(root, 0)
        return ans
