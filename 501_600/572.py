# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def is_same(t1, t2):
            if t1 is None or t2 is None:
                return t1 is None and t2 is None
            return t1.val == t2.val and is_same(t1.left, t2.left) and is_same(t1.right, t2.right)

        def is_subtree(t1, t2):
            return is_same(t1, t2) or (t1.left and is_subtree(t1.left, t2)) or (t1.right and is_subtree(t1.right, t2))

        return is_subtree(s, t)
