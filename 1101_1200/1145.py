# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        def dfs_sum(node: TreeNode):
            if not node:
                return 0
            return 1 + dfs_sum(node.left) + dfs_sum(node.right)

        def dfs_win(node: TreeNode):
            if not node:
                return True
            if node.val == x:
                l_sum, r_sum = dfs_sum(node.left), dfs_sum(node.right)
                return max(l_sum, r_sum, n - 1 - l_sum - r_sum) > n // 2
            return dfs_win(node.left) and dfs_win(node.right)

        return dfs_win(root)
