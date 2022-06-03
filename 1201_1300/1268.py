from collections import defaultdict
from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        searches = defaultdict(list)
        for product in products:
            for i in range(1, len(product) + 1):
                searches[product[:i]].append(product)
        return [searches[searchWord[:i]][:3] for i in range(1, len(searchWord) + 1)]
