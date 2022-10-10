from collections import defaultdict, Counter
from typing import List


class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        ans = []
        companies_people = defaultdict(list)
        for i, companies in sorted(enumerate(favoriteCompanies), key=lambda ic: -len(ic[1])):
            counter = Counter()
            for c in companies:
                for p in companies_people[c]:
                    counter[p] += 1
                companies_people[c].append(i)
            if all(v < len(companies) for v in counter.values()):
                ans.append(i)
        return sorted(ans)
