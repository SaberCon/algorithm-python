# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        def search(node):
            if not node:
                return None
            if node.val == val:
                return node
            if node.val < val:
                return search(node.right)
            if node.val > val:
                return search(node.left)

        return search(root)
