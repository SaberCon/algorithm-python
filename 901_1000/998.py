# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root or root.val < val:
            return TreeNode(val, root, None)
        return TreeNode(root.val, root.left, self.insertIntoMaxTree(root.right, val))
