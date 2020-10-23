class Node:
    def __init__(self, key: str, val: int, prev: 'Node' = None, next: 'Node' = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev

    def move_on(self):
        pre_next = self.next
        self.next = pre_next.next
        self.next.prev = self
        self.prev.next = pre_next
        pre_next.prev = self.prev
        self.prev = pre_next
        pre_next.next = self

    def move_back(self):
        pre_prev = self.prev
        self.prev = pre_prev.prev
        self.prev.next = self
        self.next.prev = pre_prev
        pre_prev.next = self.next
        self.next = pre_prev
        pre_prev.prev = self

    def insert_next(self, node: 'Node'):
        node.prev = self
        node.next = self.next
        self.next.prev = node
        self.next = node


class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.counts = {}
        self.head = Node('', 0)
        self.tail = Node('', 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key in self.counts:
            curr = self.counts[key]
            curr.val += 1
            while curr.next.key and curr.val > curr.next.val:
                curr.move_on()
        else:
            curr = Node(key, 1)
            self.head.insert_next(curr)
            self.counts[key] = curr

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key not in self.counts:
            return
        curr = self.counts[key]
        curr.val -= 1
        if curr.val:
            while curr.prev.key and curr.val < curr.prev.val:
                curr.move_back()
        else:
            curr.remove()
            del curr

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        return self.tail.prev.key

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        return self.head.next.key
