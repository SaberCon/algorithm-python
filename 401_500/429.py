class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        ans = []
        nodes = [root]
        while nodes:
            new_nodes = []
            ans.append([])
            for node in nodes:
                ans[-1].append(node.val)
                new_nodes += node.children
            nodes = new_nodes
        return ans
