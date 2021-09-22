# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def build(node):
            ans = [node, node]
            if node.left:
                l_min, l_max = build(node.left)
                ans[0] = l_min
                l_max.right = node
                node.left = None
            if node.right:
                r_min, r_max = build(node.right)
                ans[1] = r_max
                node.right = r_min
            return ans

        return build(root)[0]
