# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        ans = []

        def dfs(node: TreeNode, is_root: bool):
            if not node:
                return False
            if node.val in to_delete:
                dfs(node.left, True)
                dfs(node.right, True)
                return True
            if is_root:
                ans.append(node)
            if dfs(node.left, False):
                node.left = None
            if dfs(node.right, False):
                node.right = None
            return False

        dfs(root, True)
        return ans
