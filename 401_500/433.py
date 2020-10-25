def is_convertible(s1: str, s2: str):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2)) == 1


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        visited = {start}
        queue = [(start, 0)]
        while queue:
            curr_gene, count = queue.pop(0)
            if curr_gene == end:
                return count
            for next_gene in bank:
                if next_gene not in visited and is_convertible(curr_gene, next_gene):
                    visited.add(next_gene)
                    queue.append((next_gene, count + 1))
        return -1
