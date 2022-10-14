# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, values: int) -> int:
            if not node:
                return 0
            values ^= 1 << node.val
            if not node.left and not node.right:
                return bin(values).count("1") < 2
            return dfs(node.left, values) + dfs(node.right, values)

        return dfs(root, 0)
