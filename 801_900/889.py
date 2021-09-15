# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> TreeNode:
        def construct(pre_start, post_start, length):
            if length == 0:
                return None
            ans = TreeNode(preorder[pre_start])
            for i in range(post_start, post_start + length - 1):
                if postorder[i] == preorder[pre_start + 1]:
                    left_length = i - post_start + 1
                    ans.left = construct(pre_start + 1, post_start, left_length)
                    ans.right = construct(pre_start + 1 + left_length, post_start + left_length, length - 1 - left_length)
            return ans

        return construct(0, 0, len(preorder))
