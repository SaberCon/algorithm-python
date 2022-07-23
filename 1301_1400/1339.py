# Definition for a binary tree node.
from typing import Tuple, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def sum_tree(node: Optional[TreeNode]) -> int:
            return node.val + sum_tree(node.left) + sum_tree(node.right) if node else 0

        total = sum_tree(root)

        def dfs(node: Optional[TreeNode]) -> Tuple[int, int]:
            if not node:
                return 0, 0
            la, lp = dfs(node.left)
            ra, rp = dfs(node.right)
            return la + ra + node.val, max(lp, rp, (total - ra) * ra, (total - la) * la)

        return dfs(root)[1] % (10 ** 9 + 7)
