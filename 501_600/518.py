class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        amount_counts = {0: 1}
        for coin in coins:
            new_counts = amount_counts.copy()
            for coin_amount, count in amount_counts.items():
                multi_coin = coin
                while multi_coin + coin_amount <= amount:
                    new_counts.setdefault(coin_amount + multi_coin, 0)
                    new_counts[coin_amount + multi_coin] += amount_counts[coin_amount]
                    multi_coin += coin
            amount_counts = new_counts
        return amount_counts[amount] if amount in amount_counts else 0
