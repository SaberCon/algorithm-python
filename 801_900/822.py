class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        bad = {f for f, b in zip(fronts, backs) if f == b}
        good = (set(fronts) | set(backs)) - bad
        return min(good) if good else 0
