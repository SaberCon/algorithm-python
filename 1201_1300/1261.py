# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:

    def __init__(self, root: TreeNode):
        def recover(node, val):
            if node:
                node.val = val
                recover(node.left, val * 2 + 1)
                recover(node.right, val * 2 + 2)

        recover(root, 0)
        self.root = root

    def find(self, target: int) -> bool:
        def find(node, t):
            if not node:
                return False
            v = bin(node.val + 1)
            if t == v:
                return True
            return find(node.left if t.startswith(v + '0') else node.right, t)

        return find(self.root, bin(target + 1))
