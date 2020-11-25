class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        ans, left, right = 2 ** 32, -2 ** 32, -2 ** 32

        def inorder(node):
            if node.left:
                inorder(node.left)
            nonlocal ans, left, right
            left, right = right, node.val
            ans = min(ans, right - left)
            if node.right:
                inorder(node.right)

        inorder(root)
        return ans
