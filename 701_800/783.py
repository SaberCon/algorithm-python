# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        ans = 2 ** 32

        def find_min_and_max(node):
            nonlocal ans
            cmin = cmax = node.val
            if node.left:
                lmin, lmax = find_min_and_max(node.left)
                ans = min(ans, node.val - lmax)
                cmin = lmin
            if node.right:
                rmin, rmax = find_min_and_max(node.right)
                ans = min(ans, rmin - node.val)
                cmax = rmax
            return cmin, cmax

        find_min_and_max(root)
        return ans
