# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        if not quadTree1 and not quadTree2:
            return None

        def buildOrTree(tree1, tree2):
            if tree1.isLeaf:
                if tree1.val:
                    return tree1
                else:
                    return tree2
            if tree2.isLeaf:
                if tree2.val:
                    return tree2
                else:
                    return tree1
            topLeft = buildOrTree(tree1.topLeft, tree2.topLeft)
            topRight = buildOrTree(tree1.topRight, tree2.topRight)
            bottomLeft = buildOrTree(tree1.bottomLeft, tree2.bottomLeft)
            bottomRight = buildOrTree(tree1.bottomRight, tree2.bottomRight)
            if topLeft.val == topRight.val == bottomLeft.val == bottomRight.val \
                    and topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf:
                return Node(topLeft.val, True, None, None, None, None)
            else:
                return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)

        return buildOrTree(quadTree1, quadTree2)
