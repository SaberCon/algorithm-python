# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        nodes = [[0, 0]]
        is_val = True
        for c in traversal:
            if c == '-':
                if is_val:
                    nodes.append([0, 0])
                nodes[-1][0] += 1
                is_val = False
            else:
                nodes[-1][1] = 10 * nodes[-1][1] + int(c)
                is_val = True
        levels = []
        for level, val in nodes:
            node = TreeNode(val)
            if level == len(levels):
                levels.append(node)
            else:
                levels[level] = node
            if level > 0:
                parent = levels[level - 1]
                if parent.left:
                    parent.right = node
                else:
                    parent.left = node
        return levels[0]
