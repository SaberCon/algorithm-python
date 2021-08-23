# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        ans = []

        def search(node, level):
            if not node:
                return False, 0
            if node == target:
                add(node, level, level + k)
                return True, level
            found, target_level = search(node.left, level + 1)
            if found:
                if target_level == level + k:
                    ans.append(node.val)
                add(node.right, level + 1, level + k - (target_level - level))
                return True, target_level
            found, target_level = search(node.right, level + 1)
            if found:
                if target_level == level + k:
                    ans.append(node.val)
                add(node.left, level + 1, level + k - (target_level - level))
                return True, target_level
            return False, 0

        def add(node, level, target_level):
            if not node or level > target_level:
                return
            if level == target_level:
                ans.append(node.val)
            else:
                add(node.left, level + 1, target_level)
                add(node.right, level + 1, target_level)

        search(root, 0)
        return ans
