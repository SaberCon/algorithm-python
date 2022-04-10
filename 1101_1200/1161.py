# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        sums = []

        def dfs(node, level):
            if not node:
                return
            if level == len(sums):
                sums.append(node.val)
            else:
                sums[level] += node.val
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        return max(range(len(sums)), key=lambda i: (sums[i], -i)) + 1
