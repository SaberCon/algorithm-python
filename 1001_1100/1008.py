# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        current = 0

        def build_tree(limit):
            nonlocal current
            if current == len(preorder):
                return None
            val = preorder[current]
            if val > limit:
                return None
            current += 1
            return TreeNode(val, build_tree(val), build_tree(limit))

        return build_tree(1000)
