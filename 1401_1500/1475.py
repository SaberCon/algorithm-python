from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        ans = []
        for price in prices[::-1]:
            while stack and stack[-1] > price:
                stack.pop()
            ans.append(price - (stack[-1] if stack else 0))
            stack.append(price)
        return ans[::-1]
