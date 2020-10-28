class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        return self.pathSumFromRoot(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def pathSumFromRoot(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        return (root.val == sum) + self.pathSumFromRoot(root.left, sum - root.val) + self.pathSumFromRoot(root.right,
                                                                                                          sum - root.val)
