# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        def get_depth(node: TreeNode) -> int:
            if not node:
                return 0
            return max(get_depth(node.left), get_depth(node.right)) + 1

        depth = get_depth(root)
        ans = [[] for _ in range(depth)]

        def print_tree(node: TreeNode, level: int):
            if level == depth - 1:
                ans[level] += [str(node.val) if node else '', '']
                return
            print_tree(node.left if node else None, level + 1)
            print_tree(node.right if node else None, level + 1)
            curr = [''] * (len(ans[level + 1]) - len(ans[level]))
            if node:
                curr[len(curr) // 2 - 1] = str(node.val)
            ans[level] += curr

        print_tree(root, 0)
        for a in ans:
            a.pop()
        return ans
