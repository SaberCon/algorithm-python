# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ''
        left = self.tree2str(t.left)
        right = self.tree2str(t.right)
        if right:
            right = '(' + right + ')'
        if right or left:
            left = '(' + left + ')'
        return str(t.val) + left + right
