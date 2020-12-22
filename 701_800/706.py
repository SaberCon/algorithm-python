class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_range = 2069
        self.buckets = [[] for _ in range(self.key_range)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        bucket = self.buckets[self._hash(key)]
        for i, (k, _) in enumerate(self.buckets[self._hash(key)]):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        for k, v in self.buckets[self._hash(key)]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        bucket = self.buckets[self._hash(key)]
        for i, (k, _) in enumerate(self.buckets[self._hash(key)]):
            if k == key:
                bucket.pop(i)
                return

    def _hash(self, key: int) -> int:
        return key % self.key_range
