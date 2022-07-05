# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, parent: bool, grandparent: bool) -> int:
            if not node:
                return 0
            even = node.val % 2 == 0
            return (node.val if grandparent else 0) + dfs(node.left, even, parent) + dfs(node.right, even, parent)

        return dfs(root, False, False)
