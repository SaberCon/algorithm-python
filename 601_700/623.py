# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        def add_node(node, depth, is_left):
            if not node:
                if depth == d:
                    return TreeNode(v)
                else:
                    return node
            if depth < d:
                node.left = add_node(node.left, depth + 1, True)
                node.right = add_node(node.right, depth + 1, False)
                return node
            new_node = TreeNode(v)
            if is_left:
                new_node.left = node
            else:
                new_node.right = node
            return new_node

        return add_node(root, 1, True)
