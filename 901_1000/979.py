# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        def distribute(node: TreeNode):
            if not node:
                return 0, 0
            left_move, left_need = distribute(node.left)
            right_move, right_need = distribute(node.right)
            return left_move + right_move + abs(left_need) + abs(right_need), left_need + right_need + 1 - node.val

        return distribute(root)[0]
