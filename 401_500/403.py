class Solution:
    def canCross(self, stones: List[int]) -> bool:
        target = stones[-1]
        visited = {val: set() for val in stones}

        def can_cross(val, last_jump):
            if val == target:
                return True
            for i in range(-1, 2):
                next_val = val + last_jump + i
                if next_val in visited[val]:
                    continue
                visited[val].add(next_val)
                if next_val > val and next_val in visited and can_cross(next_val, last_jump + i):
                    return True
            return False

        return can_cross(0, 0)
