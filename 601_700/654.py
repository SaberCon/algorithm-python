# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        stack = []
        for num in nums + [2 ** 32]:
            curr = TreeNode(num)
            while stack and stack[-1].val < curr.val:
                stack[-1].right = curr.left
                curr.left = stack.pop()
            stack.append(curr)
        return stack[-1].left
