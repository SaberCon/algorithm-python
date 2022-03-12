class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        path = []
        size = len(bin(label)) - 2
        if size % 2 == 0:
            label = 2 ** (size - 1) + 2 ** size - label - 1
        while label > 0:
            path.append(label)
            label >>= 1
        path = path[::-1]
        for i in range(1, len(path), 2):
            path[i] = 2 ** i + 2 ** (i + 1) - path[i] - 1
        return path
