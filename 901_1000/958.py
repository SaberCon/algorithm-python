# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        end = False
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            for n in (node.left, node.right):
                if end and n:
                    return False
                elif not n:
                    end = True
                else:
                    queue.append(n)
        return True
