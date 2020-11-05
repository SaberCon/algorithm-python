# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
            return root
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
            return root
        if not root.right:
            return root.left
        min_node, new_node = self.pop_min(root.right)
        min_node.left = root.left
        min_node.right = new_node
        return min_node

    def pop_min(self, root: TreeNode) -> (TreeNode, TreeNode):
        if root.left:
            min_node, new_node = self.pop_min(root.left)
            root.left = new_node
            return min_node, root
        return root, root.right
