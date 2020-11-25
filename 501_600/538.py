class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        total = 0

        def traversal(node):
            if not node:
                return
            nonlocal total
            traversal(node.right)
            total += node.val
            node.val = total
            traversal(node.left)

        traversal(root)
        return root
