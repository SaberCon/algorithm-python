class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        prices.append(-50000)
        ans = 0
        i = 0
        while i < len(prices) - 1:
            if prices[i + 1] <= prices[i]:
                i += 1
                continue
            top = bottom = prices[i]
            while top - prices[i] <= fee and prices[i] > bottom:
                top = max(top, prices[i])
                i += 1
            ans += max(0, top - bottom - fee)
        return ans
