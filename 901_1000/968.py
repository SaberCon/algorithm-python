# Definition for a binary tree node.
from functools import cache


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        @cache
        def min_camera(node, status):
            if node is None:
                return 1000 if status == 'camera' else 0
            if status == 'camera':
                return 1 + min_camera(node.left, 'cover') + min_camera(node.right, 'cover')
            if status == 'cover':
                return min(min_camera(node, 'camera'), min_camera(node.left, 'nope') + min_camera(node.right, 'nope'))
            if status == 'nope':
                return min(min_camera(node, 'camera'),
                           min_camera(node.left, 'camera') + min_camera(node.right, 'nope'),
                           min_camera(node.left, 'nope') + min_camera(node.right, 'camera'))

        return min_camera(root, 'nope')
