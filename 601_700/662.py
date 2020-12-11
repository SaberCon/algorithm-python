# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        widths = []

        def find_max_width(node: TreeNode, width: int, level: int):
            if not node:
                return
            if level == len(widths):
                widths.append([width, width])
            else:
                widths[level][0] = min(widths[level][0], width)
                widths[level][1] = max(widths[level][1], width)
            find_max_width(node.left, 2 * width - 1, level + 1)
            find_max_width(node.right, 2 * width, level + 1)

        find_max_width(root, 1, 0)
        return max(w[1] - w[2] + 1 for w in widths)
