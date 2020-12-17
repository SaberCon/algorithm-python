# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        ans = 0

        def find_longest(node: TreeNode) -> int:
            if not node:
                return 0
            nonlocal ans
            l_longest, left = find_longest(node.left), node.left.val if node.left else 10000
            r_longest, right = find_longest(node.right), node.right.val if node.right else 10000
            if node.val == left:
                if node.val == right:
                    ans = max(ans, l_longest + r_longest + 2)
                    return max(l_longest, r_longest) + 1
                ans = max(ans, l_longest + 1)
                return l_longest + 1
            if node.val == right:
                ans = max(ans, r_longest + 1)
                return r_longest + 1
            return 0

        find_longest(root)
        return ans
