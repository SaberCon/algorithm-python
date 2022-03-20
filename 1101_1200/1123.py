# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return 0, None
            l_depth, l_node = dfs(node.left)
            r_depth, r_node = dfs(node.right)
            if l_depth < r_depth:
                return r_depth + 1, r_node
            if l_depth > r_depth:
                return l_depth + 1, l_node
            return l_depth + 1, node

        return dfs(root)[1]
