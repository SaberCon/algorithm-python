# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        if not n % 2:
            return []
        dp = [[TreeNode()]]
        for i in range(3, n + 1, 2):
            dp.append([TreeNode(0, l, r) for j in range(1, i - 1, 2) for l in dp[j // 2] for r in dp[(i - 1 - j) // 2]])
        return dp[-1]
