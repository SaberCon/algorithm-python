# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root: TreeNode) -> int:
        def find_tilt_and_sum(node):
            if not node:
                return 0, 0
            l_tilt, l_sum = find_tilt_and_sum(node.left)
            r_tilt, r_sum = find_tilt_and_sum(node.right)
            return l_tilt + r_tilt + abs(l_sum - r_sum), l_sum + r_sum + node.val

        return find_tilt_and_sum(root)[0]
