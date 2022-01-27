# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode):
            val, left, right = node.val, node.left, node.right
            if not left and not right:
                return 0, val, val
            if not left:
                diff, ma, mi = dfs(right)
            elif not right:
                diff, ma, mi = dfs(left)
            else:
                l_diff, l_ma, l_mi = dfs(left)
                r_diff, r_ma, r_mi = dfs(right)
                diff, ma, mi = max(l_diff, r_diff), max(l_ma, r_ma), min(l_mi, r_mi)
            return max(diff, abs(val - ma), abs(val - mi)), max(ma, val), min(mi, val)

        return dfs(root)[0]
