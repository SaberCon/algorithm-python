# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> (bool, bool, int, int, int, int):
            if not node:
                return True, True, 0, 0, 0, 0
            l_end, l_bst, l_total, l_best, l_mi, l_ma = dfs(node.left)
            r_end, r_bst, r_total, r_best, r_mi, r_ma = dfs(node.right)
            bst = l_bst and r_bst and (l_end or node.val > l_ma) and (r_end or node.val < r_mi)
            total = node.val + l_total + r_total
            best = max(total if bst else 0, l_best, r_best)
            mi = node.val if l_end else l_mi
            ma = node.val if r_end else r_ma
            return False, bst, total, best, mi, ma

        return dfs(root)[3]
