class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        num = len(price)
        cache = {(0,) * num: 0}

        def find_least_price(target):
            if target in cache:
                return cache[target]
            least_price = sum(p * t for p, t in zip(price, target))
            for *spec, p in special:
                next_target = tuple(t - s for s, t in zip(spec, target) if t - s >= 0)
                if p < least_price and len(next_target) == num:
                    least_price = min(least_price, p + find_least_price(next_target))
            cache[target] = least_price
            return least_price

        return find_least_price(tuple(needs))
