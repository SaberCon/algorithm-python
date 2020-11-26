class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edge_dict = {}
        for row in wall:
            total = 0
            for width in row[:-1]:
                total += width
                edge_dict[total] = edge_dict.get(total, 0) + 1
        return len(wall) - (max(edge_dict.values()) if edge_dict else 0)
