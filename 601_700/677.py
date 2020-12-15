def get_index(c) -> int:
    return ord(c) - ord('a')


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = [None] * 27

    def insert(self, key: str, val: int) -> None:
        curr = self.trie
        for c in key:
            if not curr[get_index(c)]:
                curr[get_index(c)] = [None] * 26 + [0]
            curr = curr[get_index(c)]
        curr[26] = val

    def sum(self, prefix: str) -> int:
        curr = self.trie
        for c in prefix:
            if not curr[get_index(c)]:
                return 0
            curr = curr[get_index(c)]
        stack = [curr]
        ans = 0
        while stack:
            curr = stack.pop()
            ans += curr[26]
            for p in curr:
                if p and isinstance(p, list):
                    stack.append(p)
        return ans
