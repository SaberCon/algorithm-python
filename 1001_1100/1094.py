class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        locations = [0] * (max(to for _, _, to in trips) + 1)
        for n, f, t in trips:
            locations[f] += n
            locations[t] -= n
        num = 0
        for location in locations:
            num += location
            if num > capacity:
                return False
        return True
