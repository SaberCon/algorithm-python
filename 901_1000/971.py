# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        ans = []

        def dfs(node, cur):
            if node is None:
                return cur

            if node.val != voyage[cur]:
                return -1

            nex = dfs(node.left, cur + 1)
            if nex != -1:
                nex = dfs(node.right, nex + 1)
                if nex != -1:
                    return nex
            ans.append(node.val)
            nex = dfs(node.right, cur + 1)
            if nex != -1:
                nex = dfs(node.left, nex + 1)
                if nex != -1:
                    return nex
            return -1

        return ans if dfs(root, 0) != -1 else [-1]
