class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        seen = {}
        queue = []
        cells = sum(1 << i for i, c in enumerate(cells) if c > 0)
        for i in range(n):
            cells = sum(1 << i for i in range(1, 7) if not ((1 & (cells >> (i - 1))) ^ (1 & (cells >> (i + 1)))))
            if cells in seen:
                cells = queue[(n - i - 1) % (i - seen[cells])]
                break
            seen[cells] = i
            queue.append(cells)
        return [1 & (cells >> i) for i in range(8)]
