class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def build_node(x, y, length) -> Node:
            if length == 1:
                return Node(grid[x][y], True, None, None, None, None)
            length //= 2
            sub_nodes = (build_node(x, y, length), build_node(x, y + length, length),
                         build_node(x + length, y, length), build_node(x + length, y + length, length))
            if all(n.isLeaf for n in sub_nodes) and len({n.val for n in sub_nodes}) == 1:
                return Node(grid[x][y], True, None, None, None, None)
            return Node(False, False, *sub_nodes)

        return build_node(0, 0, len(grid))
