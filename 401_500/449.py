# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ''
        vals = []
        nodes = [root]
        while nodes:
            node = nodes.pop()
            vals.append(str(node.val))
            node.right and nodes.append(node.right)
            node.left and nodes.append(node.left)
        return ' '.join(vals)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        vals = data.split(' ')
        vals.reverse()

        def build_node(ceil):
            if not vals or int(vals[-1]) > ceil:
                return None
            node = TreeNode(int(vals.pop()))
            node.left = build_node(node.val)
            node.right = build_node(ceil)
            return node

        return build_node(10001)

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
