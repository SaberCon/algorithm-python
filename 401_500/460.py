class Node:
    def __init__(self, key, val, prev=None, next=None, freq=1):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
        self.freq = freq

    def insert_prev(self, node):
        node.next = self
        node.prev = self.prev
        self.prev.next = node
        self.prev = node


class Freq:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def is_empty(self):
        return self.head.next == self.tail


class LFUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.freq_map = {}
        self.min_freq = 0

    def delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        if self.freq_map[node.freq].is_empty():
            del self.freq_map[node.freq]

    def increase(self, node):
        self.delete(node)
        if self.min_freq not in self.freq_map:
            self.min_freq += 1
        node.freq += 1
        self.freq_map.setdefault(node.freq, Freq())
        self.freq_map[node.freq].tail.insert_prev(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.increase(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.cache:
            self.increase(self.cache[key])
            self.cache[key].val = value
            return
        if len(self.cache) == self.capacity:
            del self.cache[self.freq_map[self.min_freq].head.next.key]
            self.delete(self.freq_map[self.min_freq].head.next)
        new_node = Node(key, value)
        self.cache[key] = new_node
        self.freq_map.setdefault(1, Freq())
        self.freq_map[1].tail.insert_prev(new_node)
        self.min_freq = 1


cache = LFUCache(2)
cache.put(1, 1)
cache.put(2, 2)
cache.get(1)
