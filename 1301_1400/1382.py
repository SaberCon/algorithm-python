# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []

        def traversal(node):
            if node:
                traversal(node.left)
                nodes.append(node.val)
                traversal(node.right)

        traversal(root)

        def build(start, end):
            if start >= end:
                return None
            mid = (start + end) // 2
            node = TreeNode(nodes[mid])
            node.left = build(start, mid)
            node.right = build(mid + 1, end)
            return node

        return build(0, len(nodes))
