# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        def smallest(node, suffix):
            if not node:
                return [26]
            cur = [node.val] + suffix
            if not node.left and not node.right:
                return cur
            left, right = smallest(node.left, cur), smallest(node.right, cur)
            return left if left < right else right

        return ''.join(chr(ord('a') + n) for n in smallest(root, []))
