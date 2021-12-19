# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        plus_ans = []
        minus_ans = []

        def dfs(node, row, col):
            if not node:
                return
            if col >= 0:
                if col == len(plus_ans):
                    plus_ans.append([])
                plus_ans[col].append((row, node.val))
            else:
                if col == -len(minus_ans) - 1:
                    minus_ans.append([])
                minus_ans[-col - 1].append((row, node.val))

            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)
        for nodes in minus_ans:
            nodes.sort()
        for nodes in plus_ans:
            nodes.sort()
        return [[val for row, val in nodes] for nodes in minus_ans[::-1] + plus_ans]
