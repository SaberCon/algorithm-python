# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        def zig_zag(node: TreeNode) -> (int, int, int):
            if not node:
                return 0, 0, 0
            l_max, _, l_right = zig_zag(node.left)
            r_max, r_left, _ = zig_zag(node.right)
            z_left, z_right = 1 + l_right, 1 + r_left
            return max(z_left, z_right, l_max, r_max), z_left, z_right

        return zig_zag(root)[0] - 1
