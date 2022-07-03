from typing import List


class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        weight = dict()
        lead_zero = set()
        for word in words:
            for i, ch in enumerate(word[::-1]):
                weight[ch] = weight.get(ch, 0) + 10 ** i
            if len(word) > 1:
                lead_zero.add(word[0])
        for i, ch in enumerate(result[::-1]):
            weight[ch] = weight.get(ch, 0) - 10 ** i
        if len(result) > 1:
            lead_zero.add(result[0])

        weight = sorted(list(weight.items()), key=lambda x: -abs(x[1]))
        suffix_sum_min = [0] * len(weight)
        suffix_sum_max = [0] * len(weight)
        for i in range(len(weight)):
            suffix_pos = [x[1] for x in weight[i:] if x[1] > 0]
            suffix_neg = [x[1] for x in weight[i:] if x[1] < 0]
            suffix_sum_min[i] = sum(j * elem for j, elem in enumerate(suffix_pos)) \
                + sum((9 - j) * elem for j, elem in enumerate(suffix_neg))
            suffix_sum_max[i] = sum((9 - j) * elem for j, elem in enumerate(suffix_pos)) \
                + sum(j * elem for j, elem in enumerate(suffix_neg))
        used = [0] * 10

        def dfs(pos, total):
            if pos == len(weight):
                return total == 0
            if not total + suffix_sum_min[pos] <= 0 <= total + suffix_sum_max[pos]:
                return False
            for i in range(1 if weight[pos][0] in lead_zero else 0, 10):
                if not used[i]:
                    used[i] = True
                    if dfs(pos + 1, total + weight[pos][1] * i):
                        return True
                    used[i] = False
            return False

        return dfs(0, 0)
