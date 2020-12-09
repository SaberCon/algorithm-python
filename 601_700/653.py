# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        visited = set()

        def visit(node: TreeNode) -> bool:
            if not node:
                return False
            if k - node.val in visited:
                return True
            visited.add(node.val)
            return visit(node.left) or visit(node.right)

        return visit(root)
