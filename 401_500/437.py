class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        sum_map = {0: 1}

        def path_sum(node: TreeNode, curr: int):
            if not node:
                return 0
            curr += node.val
            ans = sum_map.get(curr - sum) or 0
            sum_map[curr] = sum_map.setdefault(curr, 0) + 1
            ans += path_sum(node.left, curr) + path_sum(node.right, curr)
            sum_map[curr] -= 1
            return ans

        return path_sum(root, 0)
