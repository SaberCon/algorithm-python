class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def is_valid(num):
            time = capacity = 0
            for w in weights:
                if w > capacity:
                    time += 1
                    capacity = num
                if time > days:
                    return False
                capacity -= w
            return True

        mi, ma = max(weights), sum(weights)
        while mi < ma:
            m = (mi + ma) // 2
            if is_valid(m):
                ma = m
            else:
                mi = m + 1
        return mi
