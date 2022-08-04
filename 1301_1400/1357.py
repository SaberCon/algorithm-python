from typing import List


class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.i = 1
        self.discount = (100 - discount) / 100
        self.product_price = {product: price for product, price in zip(products, prices)}

    def getBill(self, product: List[int], amount: List[int]) -> float:
        bill = sum(self.product_price[p] * a for p, a in zip(product, amount))
        if self.i < self.n:
            self.i += 1
            return bill
        else:
            self.i = 1
            return bill * self.discount
