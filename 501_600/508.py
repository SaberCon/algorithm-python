class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        sum_count = {}

        def calc_sum(node):
            if not node:
                return 0
            subset_sum = node.val + calc_sum(node.left) + calc_sum(node.right)
            sum_count[subset_sum] = sum_count.get(subset_sum, 0) + 1
            return subset_sum

        calc_sum(root)
        top = max(sum_count.values())
        return [k for k, v in sum_count.items() if v == top]
