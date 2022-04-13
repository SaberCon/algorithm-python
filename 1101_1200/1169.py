from collections import defaultdict


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        transaction_map = defaultdict(list)
        for index, transaction in enumerate(transactions):
            name, time, amount, city = transaction.split(',')
            transaction_map[name].append((int(time), int(amount), city, index))
        ans = set()
        for name, tuples in transaction_map.items():
            tuples = sorted(tuples)
            for i, (time, amount, city, index) in enumerate(tuples):
                if amount > 1000:
                    ans.add(index)
                for j in range(i - 1, -1, -1):
                    pre_time, _, pre_city, pre_index = tuples[j]
                    if time - pre_time > 60:
                        break
                    if city != pre_city:
                        ans.add(index)
                        ans.add(pre_index)
        return [transactions[i] for i in ans]
