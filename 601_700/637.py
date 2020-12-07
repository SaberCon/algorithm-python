# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        ans = []
        stack = [(root, 0)]
        curr = 0
        while curr < len(stack):
            node, level = stack[curr]
            curr += 1
            if not node:
                continue
            stack.append((node.left, level + 1))
            stack.append((node.right, level + 1))
            if level == len(ans):
                ans.append((0, 0))
            ans[-1] = ((ans[-1][0] * ans[-1][1] + node.val) / (ans[-1][1] + 1), ans[-1][1] + 1)
        return (average for average, _ in ans)
