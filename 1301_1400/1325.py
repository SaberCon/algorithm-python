from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode]) -> bool:
            if not node:
                return True
            if dfs(node.left):
                node.left = None
            if dfs(node.right):
                node.right = None
            return not node.left and not node.right and node.val == target

        return None if dfs(root) else root
