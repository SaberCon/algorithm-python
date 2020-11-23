class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.curr = [0, 0]
        self.count = 0
        self.mode = []

    def findMode(self, root: TreeNode) -> List[int]:
        def find_mode(node: TreeNode):
            if not node:
                return
            find_mode(node.left)
            if node.val == self.curr[0]:
                self.curr[1] += 1
            else:
                self.curr = [node.val, 1]
            if self.curr[1] == self.count:
                self.mode.append(self.curr[0])
            if self.curr[1] > self.count:
                self.count = self.curr[1]
                self.mode = [self.curr[0]]
            find_mode(node.right)

        find_mode(root)
        return self.mode
