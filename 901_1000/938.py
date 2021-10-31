# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        ans = 0

        def search(node):
            nonlocal ans

            if low <= node.val <= high:
                ans += node.val
            if node.left and node.val > low:
                search(node.left)
            if node.right and node.val < high:
                search(node.right)

        search(root)
        return ans
