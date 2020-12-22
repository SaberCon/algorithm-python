class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_range = 769
        self.buckets = [[] for _ in range(self.key_range)]

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        self.buckets[self._hash(key)].append(key)

    def remove(self, key: int) -> None:
        if not self.contains(key):
            return
        self.buckets[self._hash(key)].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.buckets[self._hash(key)]

    def _hash(self, key: int) -> int:
        return key % self.key_range
