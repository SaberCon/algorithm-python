# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def to_gst(node: TreeNode, val: int):
            if not node:
                return 0
            right = to_gst(node.right, val)
            left = to_gst(node.left, val + node.val + right)
            ans = node.val + right + left
            node.val += val + right
            return ans

        to_gst(root, 0)
        return root
