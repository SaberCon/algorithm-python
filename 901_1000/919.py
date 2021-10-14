from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.queue = deque([root])
        while self.queue[0].left:
            current = self.queue[0]
            self.queue.append(current.left)
            if not current.right:
                break
            self.queue.append(current.right)
            self.queue.popleft()

    def insert(self, val: int) -> int:
        node = TreeNode(val)
        current = self.queue[0]
        self.queue.append(node)
        if not current.left:
            current.left = node
        else:
            current.right = node
            self.queue.popleft()
        return current.val

    def get_root(self) -> TreeNode:
        return self.root
