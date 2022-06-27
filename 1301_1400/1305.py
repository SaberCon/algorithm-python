from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        ans = []

        def sort(node: Optional[TreeNode], arr: List[int]):
            if not node:
                return
            sort(node.left, arr)
            arr.append(node.val)
            sort(node.right, arr)

        sort(root1, ans)
        sort(root2, ans)
        ans.sort()

        return ans
