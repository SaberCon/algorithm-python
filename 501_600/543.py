class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans = 0

        def get_diameter(node):
            left_diameter = get_diameter(node.left) + 1 if node.left else 0
            right_diameter = get_diameter(node.right) + 1 if node.right else 0
            nonlocal ans
            ans = max(ans, left_diameter + right_diameter)
            return max(left_diameter, right_diameter)

        get_diameter(root)
        return ans
