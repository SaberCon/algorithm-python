# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        def find(node):
            if node.val != root.val:
                return node.val
            if not node.left and not node.right:
                return 2 ** 32
            return min(find(node.left), find(node.right))

        ans = find(root)
        return ans if ans != 2 ** 32 else -1
