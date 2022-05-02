from random import choice
from typing import Optional


class SkiplistNode:
    def __init__(self, val=0, next=None, child=None):
        self.val = val
        self.next = next
        self.child = child


class Skiplist:

    def __init__(self):
        self.node = SkiplistNode(-1, SkiplistNode(100000))

    def search(self, target: int) -> bool:
        def do_search(node: SkiplistNode) -> bool:
            node = self.find_next_node(node, target)
            if node.next.val == target:
                return True
            if node.child:
                return do_search(node.child)
            return False

        return do_search(self.node)

    def add(self, num: int) -> None:
        def do_add(node: SkiplistNode) -> Optional[SkiplistNode]:
            node = self.find_next_node(node, num)
            if not node.child:
                new_node = SkiplistNode(num, node.next)
                node.next = new_node
                return new_node
            child_node = do_add(node.child)
            if not child_node or self.flip_coin():
                return None
            new_node = SkiplistNode(num, node.next, child_node)
            node.next = new_node
            return new_node

        child = do_add(self.node)
        if child and self.flip_coin():
            self.node = SkiplistNode(-1, SkiplistNode(num, SkiplistNode(100000), child), self.node)

    def erase(self, num: int) -> bool:
        def do_erase(node: SkiplistNode) -> bool:
            node = self.find_next_node(node, num)
            found = node.next.val == num
            if found:
                node.next = node.next.next
            if node.child:
                return do_erase(node.child)
            return found

        ans = do_erase(self.node)
        if self.node.next.val == 100000 and self.node.child:
            self.node = self.node.child
        return ans

    @staticmethod
    def find_next_node(node: SkiplistNode, num: int) -> SkiplistNode:
        while node.next.val < num:
            node = node.next
        return node

    @staticmethod
    def flip_coin() -> bool:
        return choice([True, False])
